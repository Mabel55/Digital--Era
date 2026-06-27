"""
Batch 38: Expanding Cloud Native & Go Curriculum (Modules, Channels, Helm, Operators, Istio)
"""
import json, os

NEW_COURSES_BATCH38 = {
    "Go Modules and Packages": {
        "tier": "Beginner",
        "aiRubric": "Assess Go modules basics",
        "lessons": [
            {"title": "Go Mod Init", "theory": "## Dependency Management\\nGo modules are the standard way to manage dependencies in Go projects. The `go mod init` command initializes a new module in your project directory.", "instructions": "## Task: Init a Module\\nWrite the command to initialize a new module named 'github.com/mabel/app'.", "starterCode": "go ___ ___ github.com/mabel/app", "solution": "go mod init github.com/mabel/app", "hint": "Use mod init", "rubric": "Correctly constructs the go mod init command."},
            {"title": "Importing Packages", "theory": "## Standard Library\\nGo comes with a rich standard library. You use the `import` keyword to bring packages into your program.", "instructions": "## Task: Import Formatting\\nImport the `fmt` package and use it to print 'Hello'.", "starterCode": "package main\\n\\nimport \"___\"\\n\\nfunc main() {\\n    fmt.___(\"Hello\")\\n}", "solution": "package main\\n\\nimport \"fmt\"\\n\\nfunc main() {\\n    fmt.Println(\"Hello\")\\n}", "hint": "Import fmt and use Println", "rubric": "Correctly imports fmt and calls Println."}
        ]
    },
    "Channels & Select": {
        "tier": "Intermediate",
        "aiRubric": "Assess Go concurrency patterns",
        "lessons": [
            {"title": "Channel Basics", "theory": "## Safe Communication\\nChannels are the pipes that connect concurrent goroutines. You can send values into channels from one goroutine and receive those values into another.", "instructions": "## Task: Send and Receive\\nCreate a channel of integers, send the number 42 into it, and receive it.", "starterCode": "package main\\n\\nfunc main() {\\n    ch := ___(___ int)\\n    \\n    go func() {\\n        ch ___ 42\\n    }()\\n    \\n    val := ___ ch\\n}", "solution": "package main\\n\\nfunc main() {\\n    ch := make(chan int)\\n    \\n    go func() {\\n        ch <- 42\\n    }()\\n    \\n    val := <-ch\\n}", "hint": "Use make(chan int) and the <- operator", "rubric": "Correctly uses make(chan int) and the send/receive operators."},
            {"title": "The Select Statement", "theory": "## Multiplexing\\nThe `select` statement lets a goroutine wait on multiple communication operations. It blocks until one of its cases can run.", "instructions": "## Task: Select on Two Channels\\nWrite a select statement that waits for a message from `ch1` or `ch2`.", "starterCode": "select {\\ncase msg1 := ___ ch1:\\n    fmt.Println(\"Received from ch1\", msg1)\\n___ msg2 := ___ ch2:\\n    fmt.Println(\"Received from ch2\", msg2)\\n}", "solution": "select {\\ncase msg1 := <-ch1:\\n    fmt.Println(\"Received from ch1\", msg1)\\ncase msg2 := <-ch2:\\n    fmt.Println(\"Received from ch2\", msg2)\\n}", "hint": "Use <- operator and case keyword", "rubric": "Correctly uses the case keyword and receive operator."}
        ]
    },
    "Helm Charts": {
        "tier": "Intermediate",
        "aiRubric": "Assess Helm basics",
        "lessons": [
            {"title": "The Package Manager", "theory": "## Kubernetes Templates\\nHelm is the package manager for Kubernetes. A Helm 'Chart' is a collection of files that describe a related set of Kubernetes resources.", "instructions": "## Task: Install a Chart\\nWrite the helm command to install a chart named 'my-redis' from the bitnami repository.", "starterCode": "helm ___ my-redis bitnami/___", "solution": "helm install my-redis bitnami/redis", "hint": "Use install and redis", "rubric": "Correctly uses the helm install command."},
            {"title": "Values injected in Templates", "theory": "## Customizing Deployments\\nHelm templates use the Go template engine. You can pass a `values.yaml` file to customize the Kubernetes manifests before applying.", "instructions": "## Task: Accessing Values\\nWrite the template syntax to inject the `replicaCount` from the values file.", "starterCode": "spec:\\n  replicas: {{ .___.___ }}", "solution": "spec:\\n  replicas: {{ .Values.replicaCount }}", "hint": "Use .Values.replicaCount", "rubric": "Correctly references .Values.replicaCount."}
        ]
    },
    "Advanced Kubernetes Operators": {
        "tier": "Advanced",
        "aiRubric": "Assess Operator patterns",
        "lessons": [
            {"title": "Custom Resource Definitions", "theory": "## Extending the API\\nA Custom Resource Definition (CRD) allows you to define your own object types in the Kubernetes API, just like Pods or Deployments.", "instructions": "## Task: Define a CRD Group\\nSpecify the `group` and `version` for a custom resource named `Database`.", "starterCode": "apiVersion: apiextensions.k8s.io/v1\\nkind: CustomResourceDefinition\\nmetadata:\\n  name: databases.mabel.io\\nspec:\\n  group: ___\\n  versions:\\n    - name: ___", "solution": "apiVersion: apiextensions.k8s.io/v1\\nkind: CustomResourceDefinition\\nmetadata:\\n  name: databases.mabel.io\\nspec:\\n  group: mabel.io\\n  versions:\\n    - name: v1", "hint": "Use mabel.io and v1", "rubric": "Correctly extracts the group from the name and sets version v1."},
            {"title": "Reconciliation Loop", "theory": "## The Control Loop\\nAn Operator contains a custom controller that watches your CRDs. Its core logic is the 'Reconcile' loop, which constantly ensures the current state matches the desired state.", "instructions": "## Task: Return Result\\nIn a Kubebuilder Reconcile function, return a successful empty result so the loop knows it finished correctly.", "starterCode": "func (r *DatabaseReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {\\n    // logic...\\n    return ctrl.Result{___}, ___\\n}", "solution": "func (r *DatabaseReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {\\n    // logic...\\n    return ctrl.Result{}, nil\\n}", "hint": "Return empty struct {} and nil error", "rubric": "Correctly returns ctrl.Result{} and nil."}
        ]
    },
    "Istio Service Mesh": {
        "tier": "Advanced",
        "aiRubric": "Assess Service Mesh basics",
        "lessons": [
            {"title": "Traffic Shifting", "theory": "## Canary Deployments\\nIstio allows you to split traffic between different versions of a service seamlessly, which is perfect for A/B testing or Canary releases.", "instructions": "## Task: Virtual Service Weights\\nConfigure an Istio VirtualService to send 90% of traffic to v1 and 10% to v2.", "starterCode": "route:\\n- destination:\\n    host: my-service\\n    subset: v1\\n  weight: ___\\n- destination:\\n    host: my-service\\n    subset: v2\\n  weight: ___", "solution": "route:\\n- destination:\\n    host: my-service\\n    subset: v1\\n  weight: 90\\n- destination:\\n    host: my-service\\n    subset: v2\\n  weight: 10", "hint": "Use 90 and 10", "rubric": "Correctly sets the weights to 90 and 10."},
            {"title": "Mutual TLS (mTLS)", "theory": "## Secure Communication\\nIstio can automatically encrypt all traffic between microservices in your cluster using mTLS, without changing any application code.", "instructions": "## Task: PeerAuthentication\\nSet the mTLS mode to STRICT for the entire 'default' namespace.", "starterCode": "apiVersion: security.istio.io/v1beta1\\nkind: PeerAuthentication\\nmetadata:\\n  name: default\\n  namespace: default\\nspec:\\n  mtls:\\n    mode: ___", "solution": "apiVersion: security.istio.io/v1beta1\\nkind: PeerAuthentication\\nmetadata:\\n  name: default\\n  namespace: default\\nspec:\\n  mtls:\\n    mode: STRICT", "hint": "Use STRICT", "rubric": "Sets mTLS mode to STRICT."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'cloud_native_go.json')
    
    # 1. Update cloud_native_go.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH38.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH38.items():
            tier = course_info["tier"]
            if "Cloud Native & Go" in index_data and tier in index_data["Cloud Native & Go"]:
                if new_course_name not in index_data["Cloud Native & Go"][tier]:
                    index_data["Cloud Native & Go"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 38: Added {total} lessons to Cloud Native & Go track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
