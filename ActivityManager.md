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

### 적용 가능한 위치

*   **`README.md` 파일**: 프로젝트의 메인 화면에 구조도를 보여줄 때 유용합니다.
*   **저장소(Repository)의 Wiki 페이지**: 프로젝트 아키텍처를 문서화할 때 좋습니다.
*   **이슈(Issue)나 풀 리퀘스트(Pull Request)**: 특정 기능의 구조나 변경 사항을 시각적으로 설명해야 할 때 매우 효과적입니다.

위 예시 코드를 GitHub의 Markdown 편집기에 붙여넣고 **'Preview' 탭**을 누르거나 파일을 저장하면, 해당 코드 블록이 자동으로 다이어그램 이미지로 렌더링되어 표시됩니다
