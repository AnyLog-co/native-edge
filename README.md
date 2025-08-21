# NativeEdge Blueprints for AnyLog

This repository contains all the files needed to create **Dell Native Edge blueprints** for:

- AnyLog Master  
- AnyLog Query  
- AnyLog Operator  
- AnyLog Generic Nodes  

---

## Uploading Blueprints to NativeEdge

### Step 1: Create a ZIP file
Run the following command to package the blueprint directory (replace `directoryname` with `Anylog`, `AnylogMaster4NE`, `AnylogOperator4NE`, `AnylogQuery4NE` ):

zip -r "directoryname".zip "directoryname" -x "\*/__MACOSX*" "*.DS_Store" # the latter part removes any MACOS files that will blow up the blueprint

### Step 2: Upload into NativeEdge
In NativeEdge GUI, go to Blueprints, select upload Blueprint and select appropriate .zip file.


## NOTE:  DO NOT USE SPACES in the name for the .zip.  This will cause the NativeEdge upload to fail.
