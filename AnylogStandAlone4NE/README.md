# Anylog Standalone (Native Edge)

Deploys **one VM** with three AnyLog containers on the same host:

| Node | Default TCP | Default REST |
|------|-------------|--------------|
| Master | 32048 | 32049 |
| Operator | 32148 | 32149 |
| Query | 32348 | 32349 |

Uses [AnyLog-co/docker-compose](https://github.com/AnyLog-co/docker-compose) (`anylog-master`, `anylog-operator`, `anylog-query`).

### Optional services

| Input | Default | What it deploys |
|-------|---------|-----------------|
| `include_remote_gui` | **true** | [Remote-GUI](https://github.com/AnyLog-co/Remote-GUI) — UI **http://&lt;VM&gt;:31800**, API **8080** |
| `remote_gui_conn` | `127.0.0.1:32049` | Default REST target for the GUI (master) |
| `include_grafana` | false | Grafana (`anylogco/oh-grafana`) — **http://&lt;VM&gt;:3000** |

Remote-GUI is deployed via `support/remote-gui` in the cloned docker-compose repo (`make up SERVICE=remote-gui`). If Grafana is also enabled, the GUI is configured with `GRAFANA_URL=http://127.0.0.1:3000`.

**AnylogQuery4NE** deploys query only — no Remote-GUI and no Grafana. **AnylogQueryDemo-in-a-box4NE** adds Grafana only, not Remote-GUI.

Container names: `{node_name_prefix}-master|operator|query-{guid}`.

Package as `AnylogStandAlone4NE.zip` (main file: `AnyLogStandAlone_for_NED.yaml`).
