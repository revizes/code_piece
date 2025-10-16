```mermaid
graph TD
    %% 1. Subgraph 및 Node 정의
    subgraph "Application Process"
        A[Activity/Service/BroadcastReceiver]
        B(ActivityManagerProxy)
    end

    subgraph "System Server Process"
        C{ActivityManagerService (AMS)}
        D[Activity Stack / Task]
        E[Process Management]
        F[Service Management]
        G[Broadcast Queue]
        H{WindowManagerService (WMS)}
        I{PackageManagerService (PMS)}
    end

    J((Zygote Process))
    K[New Application Process]
    L[Window/Surface]

    %% 2. Node 간의 관계(연결) 설정
    A -- IPC (Binder) --> B
    B -- Binder --> C
    C -- Manages --> D
    C -- Manages --> E
    C -- Manages --> F
    C -- Manages --> G
    C -- Interacts with --> H
    C -- Interacts with --> I
    E -- Requests Process Fork --> J
    J -- Forks --> K
    H -- Manages --> L

    %% 3. 스타일링
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
```
