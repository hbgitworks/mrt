/*

    xhandleShapeNode.cpp
    
    ////////////////////////////////////////////////////////////////////////////

    Source for xhandleShape node plugin, for use as control locators in modules
    and control rigging for modular rigging tools for maya.

    This is derived from an MPxLocatorNode, with the following
    added attributes :

    addScaleX
    addScaleY
    addScaleZ
    drawStyle
    drawAxisColour
    drawOrtho
    transformScaling
    wireframeThickness
    blendColour
    
    ////////////////////////////////////////////////////////////////////////////
    
    Feel free to modify, extend or copy for your own purpose.
    
    Written by Himanish Bhattacharya

*/

# include "xhandleShape.h"

MTypeId xhandleShape::id(0x80090);
MObject xhandleShape::aAddScale;
MObject xhandleShape::aAddScaleX;
MObject xhandleShape::aAddScaleY;
MObject xhandleShape::aAddScaleZ;
MObject xhandleShape::aDrawOrtho;
MObject xhandleShape::aDrawStyle;
MObject xhandleShape::aThickness;
MObject xhandleShape::aTransformScaling;
MObject xhandleShape::aBlendHColour;
MObject xhandleShape::aDrawAxColour;
float3& xhandleShape::dAddScale;

xhandleShape::xhandleShape() { }

xhandleShape::~xhandleShape() { }

void* xhandleShape::creator() { return new xhandleShape(); }

MStatus xhandleShape::initialize() {

    MFnNumericAttribute dsAttr;
    aDrawStyle = dsAttr.create("drawStyle", "ds", MFnNumericData::kShort);
    CHECK_MSTATUS (dsAttr.setMax(8));
    CHECK_MSTATUS (dsAttr.setMin(1));
    CHECK_MSTATUS (dsAttr.setDefault(1));
    CHECK_MSTATUS (dsAttr.setStorable(true));
    CHECK_MSTATUS (dsAttr.setReadable(true));
    CHECK_MSTATUS (dsAttr.setWritable(true));
    CHECK_MSTATUS (dsAttr.setKeyable(true));
    
    MFnEnumAttribute droAttr;
    aDrawOrtho = droAttr.create("drawOrtho", "dro");
    CHECK_MSTATUS (droAttr.addField("Off", 0));
    CHECK_MSTATUS (droAttr.addField("On", 1));
    CHECK_MSTATUS (droAttr.setDefault(1));
    CHECK_MSTATUS (droAttr.setReadable(true));
    CHECK_MSTATUS (droAttr.setStorable(true));
    CHECK_MSTATUS (droAttr.setWritable(true));
    CHECK_MSTATUS (droAttr.setKeyable(true));
    
    MFnNumericAttribute wtAttr;
    aThickness = wtAttr.create("wireframeThickness", "wt", MFnNumericData::kFloat);
    CHECK_MSTATUS (wtAttr.setMin(1.0f));
    CHECK_MSTATUS (wtAttr.setDefault(5.0f));
    CHECK_MSTATUS (wtAttr.setStorable(true));
    CHECK_MSTATUS (wtAttr.setReadable(true));
    CHECK_MSTATUS (wtAttr.setWritable(true));
    CHECK_MSTATUS (wtAttr.setKeyable(true));
    
    MFnEnumAttribute tscAttr;
    aTransformScaling = tscAttr.create("transformScaling", "tsc");
    CHECK_MSTATUS (tscAttr.addField("Off", 0));
    CHECK_MSTATUS (tscAttr.addField("On", 1));
    CHECK_MSTATUS (tscAttr.setDefault(1));
    CHECK_MSTATUS (tscAttr.setReadable(true));
    CHECK_MSTATUS (tscAttr.setStorable(true));
    CHECK_MSTATUS (tscAttr.setWritable(true));
    CHECK_MSTATUS (tscAttr.setKeyable(true));
    
    MFnNumericAttribute asxAttr;
    aAddScaleX = asxAttr.create("addScaleX", "asx", MFnNumericData::kFloat);
    CHECK_MSTATUS (asxAttr.setDefault(1.0));
    CHECK_MSTATUS (asxAttr.setStorable(true));
    CHECK_MSTATUS (asxAttr.setReadable(true));
    CHECK_MSTATUS (asxAttr.setWritable(true));
    CHECK_MSTATUS (asxAttr.setKeyable(true));
    
    MFnNumericAttribute asyAttr;
    aAddScaleY = asyAttr.create("addScaleY", "asy", MFnNumericData::kFloat);
    CHECK_MSTATUS (asyAttr.setDefault(1.0));
    CHECK_MSTATUS (asyAttr.setStorable(true));
    CHECK_MSTATUS (asyAttr.setReadable(true));
    CHECK_MSTATUS (asyAttr.setWritable(true));
    CHECK_MSTATUS (asyAttr.setKeyable(true));
    
    MFnNumericAttribute aszAttr;
    aAddScaleZ = aszAttr.create("addScaleZ", "asz", MFnNumericData::kFloat);
    CHECK_MSTATUS (aszAttr.setDefault(1.0));
    CHECK_MSTATUS (aszAttr.setStorable(true));
    CHECK_MSTATUS (aszAttr.setReadable(true));
    CHECK_MSTATUS (aszAttr.setWritable(true));
    CHECK_MSTATUS (aszAttr.setKeyable(true));

    MFnNumericAttribute asAttr;
    aAddScale = asAttr.create("addScale", "as", aAddScaleX, aAddScaleY, aAddScaleZ);
    CHECK_MSTATUS (asAttr.setDefault(1.0));
    CHECK_MSTATUS (asAttr.setStorable(true));
    CHECK_MSTATUS (asAttr.setReadable(true));
    CHECK_MSTATUS (asAttr.setWritable(true));
    CHECK_MSTATUS (asAttr.setKeyable(true));
    
    MFnEnumAttribute bhcAttr;
    aBlendHColour = bhcAttr.create("blendColour", "bhc");
    CHECK_MSTATUS (bhcAttr.addField("Off", 0));
    CHECK_MSTATUS (bhcAttr.addField("On", 1));
    CHECK_MSTATUS (bhcAttr.setDefault(0));
    CHECK_MSTATUS (bhcAttr.setReadable(true));
    CHECK_MSTATUS (bhcAttr.setStorable(true));
    CHECK_MSTATUS (bhcAttr.setWritable(true));
    CHECK_MSTATUS (bhcAttr.setKeyable(true));
    
    MFnEnumAttribute daxcAttr;
    aDrawAxColour = daxcAttr.create("drawAxisColour", "daxc");
    CHECK_MSTATUS (daxcAttr.addField("Off", 0));
    CHECK_MSTATUS (daxcAttr.addField("On", 1));
    CHECK_MSTATUS (daxcAttr.setDefault(0));
    CHECK_MSTATUS (daxcAttr.setReadable(true));
    CHECK_MSTATUS (daxcAttr.setStorable(true));
    CHECK_MSTATUS (daxcAttr.setWritable(true));
    CHECK_MSTATUS (daxcAttr.setKeyable(true));
    
    // Add the attributes
    CHECK_MSTATUS (addAttribute(aAddScale));
    CHECK_MSTATUS (addAttribute(aDrawStyle));
    CHECK_MSTATUS (addAttribute(aDrawOrtho));
    CHECK_MSTATUS (addAttribute(aThickness));
    CHECK_MSTATUS (addAttribute(aTransformScaling));
    CHECK_MSTATUS (addAttribute(aBlendHColour));
    CHECK_MSTATUS (addAttribute(aDrawAxColour));

    return MS::kSuccess;
}


MStatus xhandleShape::compute(const MPlug& plug, MDataBlock& dataBlock)
{		
		MStatus status;

		// Get the local scale attribute
        MDataHandle localScaleHandle = dataBlock.inputValue(aAddScale, &status);
        CHECK_MSTATUS (status);
        dAddScale = addScaleHandle.asFloat3();

        // Get the add scale attribute
        MDataHandle addScaleHandle = dataBlock.inputValue(aAddScale, &status);
        CHECK_MSTATUS (status);
        dAddScale = addScaleHandle.asFloat3();

        // Get the draw ortho attribute
		MDataHandle drawOrthoHandle = dataBlock.inputValue(aDrawOrtho, &status);
		CHECK_MSTATUS (status);
		dDrawOrtho = drawOrthoHandle.asBool();

		// Get the draw style attribute
        MDataHandle drawStyleHandle = dataBlock.inputValue(aDrawStyle, &status);
        CHECK_MSTATUS (status);
		dDrawStyle = drawStyleHandle.asInt();
        
		// Get the draw thickness attribute
		MDataHandle wThicknessHandle = dataBlock.inputValue(aThickness, &status);
        CHECK_MSTATUS (status);
		dThickness = wThicknessHandle.asFloat();

		// Get the transform scaling attribute
		MDataHandle trnsScalingHandle = dataBlock.inputValue(aTransformScaling, &status);
        CHECK_MSTATUS (status);
		dTransformScaling = trnsScalingHandle.asBool();
        
        // Get the draw blend colour attribute
		MDataHandle blendHClrHandle = dataBlock.inputValue(aBlendHColour, &status);
        CHECK_MSTATUS (status);
		dBlendHColour = blendHClrHandle.asBool();
        
        // Get the draw axes colour attribute
		MDataHandle drawAxClrHandle = dataBlock.inputValue(aDrawAxColour, &status);
        CHECK_MSTATUS (status);
		dDrawAxColour = drawAxClrHandle.asBool();
        
    return MS::kSuccess;
}

void xhandleShape::drawShapes(short enumType, bool drawWire, float unit_multiplier,
                                            GLfloat w_size, short drawOrtho, bool selection)
{
    MObject thisNode = thisMObject();
    
    // Get the current draw color for this node
    MPlug drawAxColourPlug(thisNode, aDrawAxColour);
    short drawAxColourValue;
    drawAxColourPlug.getValue(drawAxColourValue);
    
    // Check if draw ortho is turned on.
    MPlug drawOrthoPlug(thisNode, aDrawOrtho);
    short drawOrthoValue;
    drawOrthoPlug.getValue(drawOrthoValue);

    // Draw according to drawStyle attribute value passed to enumType.
    switch(enumType) {
    
    case 1: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        gGLFT->glVertex3f(0.0f, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        gGLFT->glVertex3f(0.0f, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
            
    case 2: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glRotatef(180.0f, 0.0f, 0.0f, 1.0f);
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glBegin(GL_POINTS);
        gGLFT->glVertex3f(0.0f, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        gGLFT->glVertex3f(0.0f, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 3: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd(); 
        gGLFT->glBegin(GL_LINE_LOOP);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 4: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        for (int i=0; i<8; i++)
            gGLFT->glVertex3f(handle_low[i][0] * unit_multiplier, handle_low[i][1] * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        for (int i=0; i<8; i++)
            gGLFT->glVertex3f(handle_low[i][0] * unit_multiplier, handle_low[i][1] * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 5: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        for (int i=0; i<16; i++)
            gGLFT->glVertex3f(handle_high[i][0] * 6.66f * unit_multiplier, handle_high[i][1] * 6.66f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        for (int i=0; i<16; i++)
            gGLFT->glVertex3f(handle_high[i][0] * 6.66f * unit_multiplier, handle_high[i][1] * 6.66f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 6: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glBegin(GL_LINE_LOOP);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_POINTS);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        for (int i=0; i<8; i++)
            gGLFT->glVertex3f(handle_low[i][0] * 0.525f * unit_multiplier, handle_low[i][1] * 0.525f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        for (int i=0; i<8; i++)
            gGLFT->glVertex3f(handle_low[i][0] * 0.525f * unit_multiplier, handle_low[i][1] * 0.525f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 7: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glBegin(GL_LINE_LOOP);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_POINTS);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd(); 
        gGLFT->glEnable(GL_POINT_SMOOTH);
        gGLFT->glLineWidth(w_size);
        gGLFT->glPointSize(w_size);
        gGLFT->glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        gGLFT->glBegin(GL_POINTS);
        for (int i=0; i<16; i++)
            gGLFT->glVertex3f(handle_high[i][0] * 3.5f * unit_multiplier, handle_high[i][1] * 3.5f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        gGLFT->glBegin(GL_LINE_LOOP);
        for (int i=0; i<16; i++)
            gGLFT->glVertex3f(handle_high[i][0] * 3.5f * unit_multiplier, handle_high[i][1] * 3.5f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        break;
    
    case 8: gGLFT->glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
        gGLFT->glLineWidth(w_size);
        if ((drawAxColourValue == 1) && (drawOrthoValue == 0) && (selection == false)){
            gGLFT->glColor3f(1.0f, 0.0f, 0.0f);
        }
        gGLFT->glBegin(GL_LINES);
        gGLFT->glVertex3f(1.0f * unit_multiplier, 0.0f, 0.0f);
        gGLFT->glVertex3f(-1.0f * unit_multiplier, 0.0f, 0.0f);
        gGLFT->glEnd();
        if ((drawAxColourValue == 1) && (drawOrthoValue == 0) && (selection == false)){
            gGLFT->glColor3f(0.0f, 0.0f, 1.0f);
        }
        gGLFT->glBegin(GL_LINES);
        gGLFT->glVertex3f(0.0f, 1.0f * unit_multiplier, 0.0f);
        gGLFT->glVertex3f(0.0f, -1.0f * unit_multiplier, 0.0f);
        gGLFT->glEnd();
        if (drawOrtho != 1) {
            if ((drawAxColourValue == 1) && (drawOrthoValue == 0) && (selection == false)){
                gGLFT->glColor3f(0.0f, 1.0f, 0.0f);
            }
        gGLFT->glBegin(GL_LINES);
        gGLFT->glVertex3f(0.0f, 0.0f, 1.0f * unit_multiplier);
        gGLFT->glVertex3f(0.0f, 0.0f, -1.0f * unit_multiplier);
        gGLFT->glEnd(); 
        break;
        }
    }
}

void xhandleShape::draw(M3dView &view, const MDagPath &path, M3dView::DisplayStyle style, M3dView::DisplayStatus status)
{   
    glPushAttrib(GL_ALL_ATTRIB_BITS);
    view.beginGL();
    
	// Get the internal unit multiplier from maya for GL draw. 
    MDistance distanceObject;
    GLfloat unit_multiplier = (float) distanceObject.uiToInternal(1.0);
    
    MObject thisNode = thisMObject();
    
    MPlug localPositionX_plug(thisNode, localPositionX);
    MPlug localPositionY_plug(thisNode, localPositionY);
    MPlug localPositionZ_plug(thisNode, localPositionZ);
    GLfloat localPositionX_value = localPositionX_plug.asFloat();
    GLfloat localPositionY_value = localPositionY_plug.asFloat();
    GLfloat localPositionZ_value = localPositionZ_plug.asFloat();
    gGLFT->glMatrixMode(GL_MODELVIEW);
    gGLFT->glTranslatef(localPositionX_value, localPositionY_value, localPositionZ_value);
    
    MPlug drawOrthoPlug(thisNode, aDrawOrtho);
    short drawOrthoValue;
    drawOrthoPlug.getValue(drawOrthoValue);
    
    if (drawOrthoValue == 1) {
        MMatrix path_r_Matrix = path.inclusiveMatrixInverse();
        gGLFT->glMultMatrixd(&(path_r_Matrix.matrix[0][0]));
        MMatrix path_t_Matrix = path.inclusiveMatrix();
        MTransformationMatrix trans_matrix(path_t_Matrix);
        MVector trans_vec = trans_matrix.getTranslation(MSpace::kTransform);
        gGLFT->glTranslated(trans_vec[0], trans_vec[1], trans_vec[2]);
    
        MDagPath cameraPath;
        view.getCamera(cameraPath);
        MMatrix camMatrix = cameraPath.inclusiveMatrix();
        MTransformationMatrix camTransMatrix(camMatrix);
        MQuaternion camRotation = camTransMatrix.rotation();
        MVector camRotAxis;
        double camRotTheta;
        camRotation.getAxisAngle(camRotAxis, camRotTheta);
        camRotTheta *= 57.2957795130f;
        gGLFT->glRotated(camRotTheta, camRotAxis[0], camRotAxis[1], camRotAxis[2]);
    }
    
    MPlug transformScalingPlug(thisNode, aTransformScaling);
    short transformScaling;
    transformScalingPlug.getValue(transformScaling);
    
    if ((transformScaling == 0) && (drawOrthoValue == 0)){
        MMatrix pathInvMatrix = path.inclusiveMatrixInverse();
        MTransformationMatrix pathInvTransMatrix(pathInvMatrix);
        double invScale[3];
        pathInvTransMatrix.getScale(invScale, MSpace::kTransform);
        gGLFT->glScaled(invScale[0], invScale[1], invScale[2]);
    }
    if ((transformScaling == 1) && (drawOrthoValue == 1)) {
        MMatrix pathMatrix = path.inclusiveMatrix();
        MTransformationMatrix pathTransMatrix(pathMatrix);
        double scale[3];
        pathTransMatrix.getScale(scale, MSpace::kTransform);
        gGLFT->glScaled(scale[0], scale[2], scale[1]);
    }
    
    MPlug localScaleX_plug(thisNode, localScaleX);
    MPlug localScaleY_plug(thisNode, localScaleY);
    MPlug localScaleZ_plug(thisNode, localScaleZ);
    GLfloat l_scaleX = localScaleX_plug.asFloat();
    GLfloat l_scaleY = localScaleY_plug.asFloat();
    GLfloat l_scaleZ = localScaleZ_plug.asFloat();
    
    MPlug addScaleX_plug(thisNode, aAddScaleX);
    MPlug addScaleY_plug(thisNode, aAddScaleY);
    MPlug addScaleZ_plug(thisNode, aAddScaleZ);
    GLfloat a_scaleX = addScaleX_plug.asFloat();
    GLfloat a_scaleY = addScaleY_plug.asFloat();
    GLfloat a_scaleZ = addScaleZ_plug.asFloat();
    
    if (drawOrthoValue == 1) {      
        gGLFT->glScalef((l_scaleX * a_scaleX), (l_scaleZ * a_scaleZ), (l_scaleY * a_scaleY));
    }
    if (drawOrthoValue == 0) {      
        gGLFT->glScalef((l_scaleX * a_scaleX), (l_scaleY * a_scaleY), (l_scaleZ * a_scaleZ));
    }
    if (drawOrthoValue == 1) {
        gGLFT->glRotatef(90.0f, 1.0f, 0.0f, 0.0f);
    }
    
    MFnDependencyNode shapeNodeFn(thisNode);
    MObject ovEnabled = shapeNodeFn.attribute("overrideEnabled");
    MObject ovColor = shapeNodeFn.attribute("overrideColor");
    MPlug ovEnabledPlug(thisNode, ovEnabled);
    MPlug ovColorPlug(thisNode, ovColor);
    bool ovEnabledValue = ovEnabledPlug.asBool();
    short ovColorValue = ovColorPlug.asShort();
    MPlug drawStylePlug(thisNode, aDrawStyle);
    short drawStyleValue = drawStylePlug.asShort();
    MPlug w_thicknessPlug(thisNode, aThickness);
    GLfloat w_size = w_thicknessPlug.asFloat();
    
    MPlug blendHColourPlug(thisNode, aBlendHColour);
    short blendHColourValue;
    blendHColourPlug.getValue(blendHColourValue);
    
    bool sel = true;
    
    if (status == M3dView::kLead)
        view.setDrawColor(18, M3dView::kActiveColors);
    if (status == M3dView::kActive)
    view.setDrawColor(15, M3dView::kActiveColors);
    if (status == M3dView::kDormant)
    {
        sel = false;
    view.setDrawColor(4, M3dView::kDormantColors);
        if (ovEnabledValue == true)
            view.setDrawColor(ovColorValue-1, M3dView::kDormantColors);
    }
    
    if (blendHColourValue == 1) {
    gGLFT->glEnable(GL_BLEND);
    gGLFT->glBlendFunc(GL_DST_COLOR, GL_SRC_COLOR);
    }
    if (blendHColourValue == 0) {
            gGLFT->glDisable(GL_BLEND);
    }

    
    if ((style == M3dView::kWireFrame) || (style == M3dView::kPoints)) 
    {   
            gGLFT->glEnable(GL_LINE_SMOOTH);
            drawShapes(drawStyleValue, true, unit_multiplier, w_size, drawOrthoValue, sel); 
    }   
    if ((style == M3dView::kFlatShaded) || (style == M3dView::kGouraudShaded)) 
    {
            gGLFT->glClearDepth(0.0);
        gGLFT->glDepthFunc(GL_ALWAYS);
            gGLFT->glEnable(GL_LINE_SMOOTH);
            drawShapes(drawStyleValue, true, unit_multiplier, w_size, drawOrthoValue, sel); 
            
    }   
    view.endGL();
    gGLFT->glPopAttrib();
}


bool xhandleShape::isBounded() const { return true; }


MBoundingBox xhandleShape::boundingBox() const
{   
    MObject thisNode = thisMObject();
    MDistance distanceObject;
    float unit_multiplier = (float) distanceObject.uiToInternal(1.0);

    MPlug localPositionX_plug(thisNode, localPositionX);
    MPlug localPositionY_plug(thisNode, localPositionY);
    MPlug localPositionZ_plug(thisNode, localPositionZ);
    float localPositionX_value = localPositionX_plug.asFloat();
    float localPositionY_value = localPositionY_plug.asFloat();
    float localPositionZ_value = localPositionZ_plug.asFloat();
    
    MVector translation_vec(localPositionX_value, localPositionY_value, localPositionZ_value);
    MTransformationMatrix t_matrix;
    t_matrix.setTranslation(translation_vec, MSpace::kTransform);
    MMatrix localPos_matrix = t_matrix.asMatrix();
    
    MPlug localScaleX_plug(thisNode, localScaleX);
    MPlug localScaleY_plug(thisNode, localScaleY);
    MPlug localScaleZ_plug(thisNode, localScaleZ);
    float l_scaleX = localScaleX_plug.asFloat();
    float l_scaleY = localScaleY_plug.asFloat();
    float l_scaleZ = localScaleZ_plug.asFloat();
    
    MPlug addScaleX_plug(thisNode, aAddScaleX);
    MPlug addScaleY_plug(thisNode, aAddScaleY);
    MPlug addScaleZ_plug(thisNode, aAddScaleZ);
    float a_scaleX = addScaleX_plug.asFloat();
    float a_scaleY = addScaleY_plug.asFloat();
    float a_scaleZ = addScaleZ_plug.asFloat();

    MPlug drawStylePlug(thisNode, aDrawStyle);
    short drawStyleValue = drawStylePlug.asShort();

    MPlug drawOrthoPlug(thisNode, aDrawOrtho);
    short drawOrthoValue;
    drawOrthoPlug.getValue(drawOrthoValue);

    float c1[3] = {-1.0, 0.0, 1.0};
    float c2[3] = {1.0, 0.0, -1.0};

    if ((drawOrthoValue == 0) && (drawStyleValue == 8)) {
        c1[1] = 1.0;
        c2[1] = -1.0;
    }
    if (drawOrthoValue == 1) {
        c1[1] = 1.0;
        c2[1] = -1.0;
    }

    c1[0] = c1[0] * (l_scaleX * a_scaleX);
    c2[0] = c2[0] * (l_scaleX * a_scaleX);
    c1[1] = c1[1] * (l_scaleY * a_scaleY);
    c2[1] = c2[1] * (l_scaleY * a_scaleY);
    c1[2] = c1[2] * (l_scaleZ * a_scaleZ);
    c2[2] = c2[2] * (l_scaleZ * a_scaleZ);

    MPoint corner1(c1[0], c1[1], c1[2]);
    MPoint corner2(c2[0], c2[1], c2[2]);

    corner1 = corner1 * unit_multiplier;
    corner2 = corner2 * unit_multiplier;

    MBoundingBox b_box(corner1, corner2);
    b_box.transformUsing(localPos_matrix);

    MPlug transformScalingPlug(thisNode, aTransformScaling);
    short transformScaling;
    transformScalingPlug.getValue(transformScaling);

    if (transformScaling == 0) {
        MDagPath path;
        MFnDagNode pathNode(thisNode);
        pathNode.getPath(path);
        MMatrix pathMatrix = path.inclusiveMatrixInverse();
        MTransformationMatrix pathTransMatrix(pathMatrix);
        double scale[3];
        pathTransMatrix.getScale(scale, MSpace::kTransform);
        MTransformationMatrix s_matrix;
        s_matrix.setScale(scale, MSpace::kTransform);
        MMatrix scale_matrix = s_matrix.asMatrix();
        b_box.transformUsing(scale_matrix);
    }
    return b_box;
}


