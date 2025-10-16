```mermaid
graph TD
    subgraph "Application Process"
        A[Activity/Service/BroadcastReceiver] -- IPC (Binder) --> B(ActivityManagerProxy)
    end

    B -- Binder --> C{ActivityManagerService (AMS)}

    subgraph "System Server Process"
        C -- Manages --> D[Activity Stack / Task]
        C -- Manages --> E[Process Management]
        C -- Manages --> F[Service Management]
        C -- Manages --> G[Broadcast Queue]
        C -- Interacts with --> H{WindowManagerService (WMS)}
        C -- Interacts with --> I{PackageManagerService (PMS)}
    end

    E -- Requests Process Fork --> J((Zygote Process))
    J -- Forks --> K[New Application Process]
    H -- Manages --> L[Window/Surface]

    style C fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
```
