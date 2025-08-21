This repo contains all the files needed to create Dell Native Edge blueprints for Anylog Master/Query/Operator/generic nodes.

To upload to nativeedge do the following

Step 1:  Create zip file for Master/query/operator 
zip -r "directoryname".zip "directoryname" -x "\*/__MACOSX*" "*.DS_Store" # the latter part removes any MACOS files that will blow up the blueprint

Step2: Upload into NativeEdge
In NativeEdge GUI, go to Blueprints, select upload Blueprint and select appropriate .zip file.


NOTE:  DO NOT USE SPACES in the name for the .zip.  This will cause the NativeEdge upload to fail.

