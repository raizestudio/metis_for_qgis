<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyDrawingHints="0" labelsEnabled="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" simplifyMaxScale="1" maxScale="0" readOnly="0" version="3.4.4-Madeira" simplifyAlgorithm="0" simplifyDrawingTol="1" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" forceraster="0" type="RuleRenderer">
    <rules key="{450d9a9c-2d59-4f04-bbb8-076bd621d1ab}">
      <rule symbol="0" filter="&quot;ST_GENRE&quot; = 'CLIENT' and  &quot;AD_NBLHAB&quot; &lt; 4" key="{a6cb20f9-abd8-4004-b845-763247d07a05}" label="CLIENT"/>
      <rule symbol="1" filter="&quot;ST_GENRE&quot; = 'PM'" key="{d646fcbb-4b65-4d53-8398-4b9389011c6b}" checkstate="0" label="PM"/>
      <rule symbol="2" filter=" &quot;S_NBPRISE&quot;  >= 4 " key="{d00b7f33-da40-4004-8d53-a2b58f784430}" label="IMB"/>
    </rules>
    <symbols>
      <symbol alpha="1" force_rhr="0" name="0" type="marker" clip_to_extent="1">
        <layer locked="0" pass="0" enabled="1" class="SvgMarker">
          <prop v="0" k="angle"/>
          <prop v="152,151,151,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="accommodation/accommodation_house.svg" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="5" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" force_rhr="0" name="1" type="marker" clip_to_extent="1">
        <layer locked="0" pass="0" enabled="1" class="SvgMarker">
          <prop v="0" k="angle"/>
          <prop v="255,5,1,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="symbol/red-marker.svg" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="10" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="2" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" force_rhr="0" name="2" type="marker" clip_to_extent="1">
        <layer locked="0" pass="0" enabled="1" class="SvgMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="0" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="gpsicons/city_building.svg" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="3" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontItalic="0" fontStrikeout="0" fontWordSpacing="0" previewBkgrdColor="#ffffff" isExpression="1" fontSize="7.8" multilineHeight="1" fontFamily="MS Shell Dlg 2" blendMode="0" fontCapitals="0" fieldName=" &quot;ad_numero&quot;  ||  ', '  ||   &quot;ad_tvoie&quot;  ||   ' '||  &quot;ad_nomvoie&quot; " textColor="0,0,0,255" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" namedStyle="Normal" useSubstitutions="0" fontWeight="50" fontLetterSpacing="0" textOpacity="1" fontSizeUnit="Point">
        <text-buffer bufferSize="1" bufferBlendMode="0" bufferSizeUnits="MM" bufferOpacity="1" bufferColor="255,255,255,255" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="0" bufferNoFill="0" bufferJoinStyle="128"/>
        <background shapeSVGFile="" shapeBorderWidth="0" shapeBorderWidthUnit="MM" shapeRotation="0" shapeType="0" shapeOffsetY="0" shapeJoinStyle="64" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeBlendMode="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeOffsetUnit="MM" shapeRadiiX="0" shapeDraw="0" shapeSizeY="0" shapeOffsetX="0" shapeOpacity="1" shapeSizeX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255"/>
        <shadow shadowBlendMode="6" shadowColor="0,0,0,255" shadowOpacity="0.7" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowScale="100" shadowDraw="0" shadowOffsetAngle="135" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowOffsetDist="1" shadowOffsetGlobal="1" shadowRadius="1.5" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <substitutions/>
      </text-style>
      <text-format autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" decimals="3" plussign="0" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" formatNumbers="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" wrapChar="" placeDirectionSymbol="0"/>
      <placement predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleOut="-25" dist="1" quadOffset="2" placement="0" rotationAngle="0" maxCurvedCharAngleIn="25" offsetType="0" placementFlags="10" fitInPolygonOnly="0" preserveRotation="1" yOffset="0" offsetUnits="MapUnit" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" repeatDistance="0" centroidWhole="0" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" repeatDistanceUnits="MM" distUnits="MM"/>
      <rendering scaleMax="10000000" obstacleType="0" obstacleFactor="1" minFeatureSize="0" fontLimitPixelSize="0" maxNumLabels="2000" scaleVisibility="0" obstacle="1" drawLabels="1" upsidedownLabels="0" fontMinPixelSize="3" fontMaxPixelSize="10000" labelPerPart="0" mergeLines="0" zIndex="0" limitNumLabels="0" displayAll="0" scaleMin="1"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>COALESCE( "AD_IDATIMN", '&lt;NULL>' )</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory backgroundColor="#ffffff" opacity="1" lineSizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" scaleDependency="Area" width="15" penAlpha="255" penWidth="0" minScaleDenominator="0" scaleBasedVisibility="0" barWidth="5" labelPlacementMethod="XHeight" lineSizeType="MM" penColor="#000000" height="15" enabled="0" maxScaleDenominator="1e+08" sizeType="MM" diagramOrientation="Up" sizeScale="3x:0,0,0,0,0,0" minimumSize="0" rotationOffset="270">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" obstacle="0" priority="0" linePlacementFlags="18" placement="0" dist="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="oid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_code">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_hexacle">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_tvoie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_nomvoie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_numero">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_rep">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_insee">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_postal">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_alias">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_x_ban">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_y_ban">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_commune">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_nat">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_nblhab">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_nblpro">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_isole">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_racc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_itypeim">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_imneuf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_idatimn">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_comment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sf_code">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sf_type">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_genre">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_statut">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_codeext">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_prop">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_gest">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_proptyp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="st_typephy">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_bpnro">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_bpsro">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_nbtech">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_nbprise">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_ldist3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_ldist2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_ldist1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_lracc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_ecoracc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_ecoprise">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_lot">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_prio">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_creadat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_majdate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ad_majsrc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="s_geom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="oid" name=""/>
    <alias index="1" field="ad_code" name=""/>
    <alias index="2" field="ad_hexacle" name=""/>
    <alias index="3" field="ad_tvoie" name=""/>
    <alias index="4" field="ad_nomvoie" name=""/>
    <alias index="5" field="ad_numero" name=""/>
    <alias index="6" field="ad_rep" name=""/>
    <alias index="7" field="ad_insee" name=""/>
    <alias index="8" field="ad_postal" name=""/>
    <alias index="9" field="ad_alias" name=""/>
    <alias index="10" field="ad_x_ban" name=""/>
    <alias index="11" field="ad_y_ban" name=""/>
    <alias index="12" field="ad_commune" name=""/>
    <alias index="13" field="ad_nat" name=""/>
    <alias index="14" field="ad_nblhab" name=""/>
    <alias index="15" field="ad_nblpro" name=""/>
    <alias index="16" field="ad_isole" name=""/>
    <alias index="17" field="ad_racc" name=""/>
    <alias index="18" field="ad_itypeim" name=""/>
    <alias index="19" field="ad_imneuf" name=""/>
    <alias index="20" field="ad_idatimn" name=""/>
    <alias index="21" field="ad_comment" name=""/>
    <alias index="22" field="sf_code" name=""/>
    <alias index="23" field="sf_type" name=""/>
    <alias index="24" field="st_genre" name=""/>
    <alias index="25" field="st_statut" name=""/>
    <alias index="26" field="st_codeext" name=""/>
    <alias index="27" field="st_prop" name=""/>
    <alias index="28" field="st_gest" name=""/>
    <alias index="29" field="st_proptyp" name=""/>
    <alias index="30" field="st_typephy" name=""/>
    <alias index="31" field="s_bpnro" name=""/>
    <alias index="32" field="s_bpsro" name=""/>
    <alias index="33" field="s_nbtech" name=""/>
    <alias index="34" field="s_nbprise" name=""/>
    <alias index="35" field="s_ldist3" name=""/>
    <alias index="36" field="s_ldist2" name=""/>
    <alias index="37" field="s_ldist1" name=""/>
    <alias index="38" field="s_lracc" name=""/>
    <alias index="39" field="s_ecoracc" name=""/>
    <alias index="40" field="s_ecoprise" name=""/>
    <alias index="41" field="s_lot" name=""/>
    <alias index="42" field="s_prio" name=""/>
    <alias index="43" field="ad_creadat" name=""/>
    <alias index="44" field="ad_majdate" name=""/>
    <alias index="45" field="ad_majsrc" name=""/>
    <alias index="46" field="s_geom" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="oid"/>
    <default applyOnUpdate="0" expression="" field="ad_code"/>
    <default applyOnUpdate="0" expression="" field="ad_hexacle"/>
    <default applyOnUpdate="0" expression="" field="ad_tvoie"/>
    <default applyOnUpdate="0" expression="" field="ad_nomvoie"/>
    <default applyOnUpdate="0" expression="" field="ad_numero"/>
    <default applyOnUpdate="0" expression="" field="ad_rep"/>
    <default applyOnUpdate="0" expression="" field="ad_insee"/>
    <default applyOnUpdate="0" expression="" field="ad_postal"/>
    <default applyOnUpdate="0" expression="" field="ad_alias"/>
    <default applyOnUpdate="0" expression="" field="ad_x_ban"/>
    <default applyOnUpdate="0" expression="" field="ad_y_ban"/>
    <default applyOnUpdate="0" expression="" field="ad_commune"/>
    <default applyOnUpdate="0" expression="" field="ad_nat"/>
    <default applyOnUpdate="0" expression="" field="ad_nblhab"/>
    <default applyOnUpdate="0" expression="" field="ad_nblpro"/>
    <default applyOnUpdate="0" expression="" field="ad_isole"/>
    <default applyOnUpdate="0" expression="" field="ad_racc"/>
    <default applyOnUpdate="0" expression="" field="ad_itypeim"/>
    <default applyOnUpdate="0" expression="" field="ad_imneuf"/>
    <default applyOnUpdate="0" expression="" field="ad_idatimn"/>
    <default applyOnUpdate="0" expression="" field="ad_comment"/>
    <default applyOnUpdate="0" expression="" field="sf_code"/>
    <default applyOnUpdate="0" expression="" field="sf_type"/>
    <default applyOnUpdate="0" expression="" field="st_genre"/>
    <default applyOnUpdate="0" expression="" field="st_statut"/>
    <default applyOnUpdate="0" expression="" field="st_codeext"/>
    <default applyOnUpdate="0" expression="" field="st_prop"/>
    <default applyOnUpdate="0" expression="" field="st_gest"/>
    <default applyOnUpdate="0" expression="" field="st_proptyp"/>
    <default applyOnUpdate="0" expression="" field="st_typephy"/>
    <default applyOnUpdate="0" expression="" field="s_bpnro"/>
    <default applyOnUpdate="0" expression="" field="s_bpsro"/>
    <default applyOnUpdate="0" expression="" field="s_nbtech"/>
    <default applyOnUpdate="0" expression="" field="s_nbprise"/>
    <default applyOnUpdate="0" expression="" field="s_ldist3"/>
    <default applyOnUpdate="0" expression="" field="s_ldist2"/>
    <default applyOnUpdate="0" expression="" field="s_ldist1"/>
    <default applyOnUpdate="0" expression="" field="s_lracc"/>
    <default applyOnUpdate="0" expression="" field="s_ecoracc"/>
    <default applyOnUpdate="0" expression="" field="s_ecoprise"/>
    <default applyOnUpdate="0" expression="" field="s_lot"/>
    <default applyOnUpdate="0" expression="" field="s_prio"/>
    <default applyOnUpdate="0" expression="" field="ad_creadat"/>
    <default applyOnUpdate="0" expression="" field="ad_majdate"/>
    <default applyOnUpdate="0" expression="" field="ad_majsrc"/>
    <default applyOnUpdate="0" expression="" field="s_geom"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="oid" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_code" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_hexacle" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_tvoie" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_nomvoie" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_numero" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_rep" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_insee" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_postal" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_alias" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_x_ban" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_y_ban" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_commune" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_nat" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_nblhab" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_nblpro" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_isole" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_racc" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_itypeim" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_imneuf" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_idatimn" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_comment" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="sf_code" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="sf_type" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_genre" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_statut" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_codeext" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_prop" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_gest" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_proptyp" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="st_typephy" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_bpnro" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_bpsro" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_nbtech" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_nbprise" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_ldist3" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_ldist2" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_ldist1" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_lracc" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_ecoracc" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_ecoprise" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_lot" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_prio" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_creadat" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_majdate" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="ad_majsrc" exp_strength="0"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" field="s_geom" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="oid" desc=""/>
    <constraint exp="" field="ad_code" desc=""/>
    <constraint exp="" field="ad_hexacle" desc=""/>
    <constraint exp="" field="ad_tvoie" desc=""/>
    <constraint exp="" field="ad_nomvoie" desc=""/>
    <constraint exp="" field="ad_numero" desc=""/>
    <constraint exp="" field="ad_rep" desc=""/>
    <constraint exp="" field="ad_insee" desc=""/>
    <constraint exp="" field="ad_postal" desc=""/>
    <constraint exp="" field="ad_alias" desc=""/>
    <constraint exp="" field="ad_x_ban" desc=""/>
    <constraint exp="" field="ad_y_ban" desc=""/>
    <constraint exp="" field="ad_commune" desc=""/>
    <constraint exp="" field="ad_nat" desc=""/>
    <constraint exp="" field="ad_nblhab" desc=""/>
    <constraint exp="" field="ad_nblpro" desc=""/>
    <constraint exp="" field="ad_isole" desc=""/>
    <constraint exp="" field="ad_racc" desc=""/>
    <constraint exp="" field="ad_itypeim" desc=""/>
    <constraint exp="" field="ad_imneuf" desc=""/>
    <constraint exp="" field="ad_idatimn" desc=""/>
    <constraint exp="" field="ad_comment" desc=""/>
    <constraint exp="" field="sf_code" desc=""/>
    <constraint exp="" field="sf_type" desc=""/>
    <constraint exp="" field="st_genre" desc=""/>
    <constraint exp="" field="st_statut" desc=""/>
    <constraint exp="" field="st_codeext" desc=""/>
    <constraint exp="" field="st_prop" desc=""/>
    <constraint exp="" field="st_gest" desc=""/>
    <constraint exp="" field="st_proptyp" desc=""/>
    <constraint exp="" field="st_typephy" desc=""/>
    <constraint exp="" field="s_bpnro" desc=""/>
    <constraint exp="" field="s_bpsro" desc=""/>
    <constraint exp="" field="s_nbtech" desc=""/>
    <constraint exp="" field="s_nbprise" desc=""/>
    <constraint exp="" field="s_ldist3" desc=""/>
    <constraint exp="" field="s_ldist2" desc=""/>
    <constraint exp="" field="s_ldist1" desc=""/>
    <constraint exp="" field="s_lracc" desc=""/>
    <constraint exp="" field="s_ecoracc" desc=""/>
    <constraint exp="" field="s_ecoprise" desc=""/>
    <constraint exp="" field="s_lot" desc=""/>
    <constraint exp="" field="s_prio" desc=""/>
    <constraint exp="" field="ad_creadat" desc=""/>
    <constraint exp="" field="ad_majdate" desc=""/>
    <constraint exp="" field="ad_majsrc" desc=""/>
    <constraint exp="" field="s_geom" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" sortExpression="&quot;ST_GENRE&quot;" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" name="oid" type="field" width="-1"/>
      <column hidden="0" name="ad_code" type="field" width="-1"/>
      <column hidden="0" name="ad_hexacle" type="field" width="-1"/>
      <column hidden="0" name="ad_tvoie" type="field" width="-1"/>
      <column hidden="0" name="ad_nomvoie" type="field" width="-1"/>
      <column hidden="0" name="ad_numero" type="field" width="-1"/>
      <column hidden="0" name="ad_rep" type="field" width="-1"/>
      <column hidden="0" name="ad_insee" type="field" width="-1"/>
      <column hidden="0" name="ad_postal" type="field" width="-1"/>
      <column hidden="0" name="ad_alias" type="field" width="-1"/>
      <column hidden="0" name="ad_x_ban" type="field" width="-1"/>
      <column hidden="0" name="ad_y_ban" type="field" width="-1"/>
      <column hidden="0" name="ad_commune" type="field" width="-1"/>
      <column hidden="0" name="ad_nat" type="field" width="-1"/>
      <column hidden="0" name="ad_nblhab" type="field" width="-1"/>
      <column hidden="0" name="ad_nblpro" type="field" width="-1"/>
      <column hidden="0" name="ad_isole" type="field" width="-1"/>
      <column hidden="0" name="ad_racc" type="field" width="-1"/>
      <column hidden="0" name="ad_itypeim" type="field" width="-1"/>
      <column hidden="0" name="ad_imneuf" type="field" width="-1"/>
      <column hidden="0" name="ad_idatimn" type="field" width="-1"/>
      <column hidden="0" name="ad_comment" type="field" width="-1"/>
      <column hidden="0" name="sf_code" type="field" width="-1"/>
      <column hidden="0" name="sf_type" type="field" width="-1"/>
      <column hidden="0" name="st_genre" type="field" width="-1"/>
      <column hidden="0" name="st_statut" type="field" width="-1"/>
      <column hidden="0" name="st_codeext" type="field" width="-1"/>
      <column hidden="0" name="st_prop" type="field" width="-1"/>
      <column hidden="0" name="st_gest" type="field" width="-1"/>
      <column hidden="0" name="st_proptyp" type="field" width="-1"/>
      <column hidden="0" name="st_typephy" type="field" width="-1"/>
      <column hidden="0" name="s_bpnro" type="field" width="-1"/>
      <column hidden="0" name="s_bpsro" type="field" width="-1"/>
      <column hidden="0" name="s_nbtech" type="field" width="-1"/>
      <column hidden="0" name="s_nbprise" type="field" width="-1"/>
      <column hidden="0" name="s_ldist3" type="field" width="-1"/>
      <column hidden="0" name="s_ldist2" type="field" width="-1"/>
      <column hidden="0" name="s_ldist1" type="field" width="-1"/>
      <column hidden="0" name="s_lracc" type="field" width="-1"/>
      <column hidden="0" name="s_ecoracc" type="field" width="-1"/>
      <column hidden="0" name="s_ecoprise" type="field" width="-1"/>
      <column hidden="0" name="s_lot" type="field" width="-1"/>
      <column hidden="0" name="s_prio" type="field" width="-1"/>
      <column hidden="0" name="ad_creadat" type="field" width="-1"/>
      <column hidden="0" name="ad_majdate" type="field" width="-1"/>
      <column hidden="0" name="ad_majsrc" type="field" width="-1"/>
      <column hidden="0" name="s_geom" type="field" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>.</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="ad_alias"/>
    <field editable="1" name="ad_code"/>
    <field editable="1" name="ad_comment"/>
    <field editable="1" name="ad_commune"/>
    <field editable="1" name="ad_creadat"/>
    <field editable="1" name="ad_hexacle"/>
    <field editable="1" name="ad_idatimn"/>
    <field editable="1" name="ad_imneuf"/>
    <field editable="1" name="ad_insee"/>
    <field editable="1" name="ad_isole"/>
    <field editable="1" name="ad_itypeim"/>
    <field editable="1" name="ad_majdate"/>
    <field editable="1" name="ad_majsrc"/>
    <field editable="1" name="ad_nat"/>
    <field editable="1" name="ad_nblhab"/>
    <field editable="1" name="ad_nblpro"/>
    <field editable="1" name="ad_nomvoie"/>
    <field editable="1" name="ad_numero"/>
    <field editable="1" name="ad_postal"/>
    <field editable="1" name="ad_racc"/>
    <field editable="1" name="ad_rep"/>
    <field editable="1" name="ad_tvoie"/>
    <field editable="1" name="ad_x_ban"/>
    <field editable="1" name="ad_y_ban"/>
    <field editable="1" name="oid"/>
    <field editable="1" name="s_bpnro"/>
    <field editable="1" name="s_bpsro"/>
    <field editable="1" name="s_ecoprise"/>
    <field editable="1" name="s_ecoracc"/>
    <field editable="1" name="s_geom"/>
    <field editable="1" name="s_ldist1"/>
    <field editable="1" name="s_ldist2"/>
    <field editable="1" name="s_ldist3"/>
    <field editable="1" name="s_lot"/>
    <field editable="1" name="s_lracc"/>
    <field editable="1" name="s_nbprise"/>
    <field editable="1" name="s_nbtech"/>
    <field editable="1" name="s_prio"/>
    <field editable="1" name="sf_code"/>
    <field editable="1" name="sf_type"/>
    <field editable="1" name="st_codeext"/>
    <field editable="1" name="st_genre"/>
    <field editable="1" name="st_gest"/>
    <field editable="1" name="st_prop"/>
    <field editable="1" name="st_proptyp"/>
    <field editable="1" name="st_statut"/>
    <field editable="1" name="st_typephy"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ad_alias"/>
    <field labelOnTop="0" name="ad_code"/>
    <field labelOnTop="0" name="ad_comment"/>
    <field labelOnTop="0" name="ad_commune"/>
    <field labelOnTop="0" name="ad_creadat"/>
    <field labelOnTop="0" name="ad_hexacle"/>
    <field labelOnTop="0" name="ad_idatimn"/>
    <field labelOnTop="0" name="ad_imneuf"/>
    <field labelOnTop="0" name="ad_insee"/>
    <field labelOnTop="0" name="ad_isole"/>
    <field labelOnTop="0" name="ad_itypeim"/>
    <field labelOnTop="0" name="ad_majdate"/>
    <field labelOnTop="0" name="ad_majsrc"/>
    <field labelOnTop="0" name="ad_nat"/>
    <field labelOnTop="0" name="ad_nblhab"/>
    <field labelOnTop="0" name="ad_nblpro"/>
    <field labelOnTop="0" name="ad_nomvoie"/>
    <field labelOnTop="0" name="ad_numero"/>
    <field labelOnTop="0" name="ad_postal"/>
    <field labelOnTop="0" name="ad_racc"/>
    <field labelOnTop="0" name="ad_rep"/>
    <field labelOnTop="0" name="ad_tvoie"/>
    <field labelOnTop="0" name="ad_x_ban"/>
    <field labelOnTop="0" name="ad_y_ban"/>
    <field labelOnTop="0" name="oid"/>
    <field labelOnTop="0" name="s_bpnro"/>
    <field labelOnTop="0" name="s_bpsro"/>
    <field labelOnTop="0" name="s_ecoprise"/>
    <field labelOnTop="0" name="s_ecoracc"/>
    <field labelOnTop="0" name="s_geom"/>
    <field labelOnTop="0" name="s_ldist1"/>
    <field labelOnTop="0" name="s_ldist2"/>
    <field labelOnTop="0" name="s_ldist3"/>
    <field labelOnTop="0" name="s_lot"/>
    <field labelOnTop="0" name="s_lracc"/>
    <field labelOnTop="0" name="s_nbprise"/>
    <field labelOnTop="0" name="s_nbtech"/>
    <field labelOnTop="0" name="s_prio"/>
    <field labelOnTop="0" name="sf_code"/>
    <field labelOnTop="0" name="sf_type"/>
    <field labelOnTop="0" name="st_codeext"/>
    <field labelOnTop="0" name="st_genre"/>
    <field labelOnTop="0" name="st_gest"/>
    <field labelOnTop="0" name="st_prop"/>
    <field labelOnTop="0" name="st_proptyp"/>
    <field labelOnTop="0" name="st_statut"/>
    <field labelOnTop="0" name="st_typephy"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE( "AD_IDATIMN", '&lt;NULL>' )</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
