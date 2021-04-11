
import sys

import os
import nuke

# SET TOOLS PATH
global toolsPath
toolsPath = os.path.dirname(os.path.normpath(__file__))

# RETURN EVERYTHING IN DIRECTORY AND CHECK FOR THE DIRECTORY ONLY
onlyDir = [ f for f in os.listdir( toolsPath ) if os.path.isdir( os.path.join( toolsPath, f ))]
for eachDir in onlyDir:
    #ADD THE DIRECTORY AS PLUGIN
    print eachDir
    nuke.pluginAddPath( eachDir )
    sys.path.append( os.path.join( toolsPath, eachDir ) )
'''
import fileExplorer
import readFromWrite
import reloadRead
    

# Gizmo Callbacks
import projectControl
import ColorMatte_Callbacks
'''