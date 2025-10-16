```mermaid
graph TD
    subgraph "Application Process"
        A[Activity/Service/BroadcastReceiver] -- IPC (Binder) --> B(ActivityManagerProxy)
    end

    subgraph "System Server Process"
        C{ActivityManagerService (AMS)}
        H{WindowManagerService (WMS)}
        I{PackageManagerService (PMS)}

        C -- Manages --> D[Activity Stack / Task]
        C -- Manages --> E[Process Management]
        C -- Manages --> F[Service Management]
        C -- Manages --> G[Broadcast Queue]
        C -- Interacts with --> H
        C -- Interacts with --> I
    end

    J((Zygote Process))
    K[New Application Process]
    L[Window/Surface]

    B -- Binder --> C
    E -- Requests Process Fork --> J
    J -- Forks --> K
    H -- Manages --> L

    style C fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
```
