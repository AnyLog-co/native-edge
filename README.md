# Dell Automation Platform Blueprints for AnyLog

This repository contains blueprint packages for **Dell Automation Platform** (DAP) / NativeEdge endpoints, using TOSCA DSL **`dell_1_1`**.

| Package | Role |
|---------|------|
| `AnyLog` | Generic AnyLog node |
| `AnylogMaster4NE` | Master node |
| `AnylogOperator4NE` | Operator node |
| `AnylogQuery4NE` | Query node |
| `AnylogQueryDemo-in-a-box4NE` | Query + Grafana |
| `AnylogStandAlone4NE` | Master + operator + query (+ optional Remote-GUI / Grafana) |

Requires **Dell Automation Platform orchestrator 1.1.0.0** (or compatible) with `dell-plugin`, `dell-utilities-plugin`, `dell-fabric-plugin`, and `dell-ansible-plugin` installed.

---

## Uploading blueprints

### Step 1: Create a ZIP file

Replace `directoryname` with one of the package folders above:

```bash
zip -r "directoryname".zip "directoryname" -x "*/__MACOSX*" "*.DS_Store"
```

### Step 2: Upload to the orchestrator

In the **Dell Automation Platform** UI, go to **Blueprints** → **Upload blueprint** and select the `.zip` file.

**Note:** Do not use spaces in the zip filename; upload may fail.
