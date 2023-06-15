# k3dcluster_tester

test repo

argocd app create --name lulu --repo <https://github.com/vrahmanov/k3dcluster_tester> --dest-server <https://kubernetes.default.svc> --dest-namespace default --path myappbomba && argocd app sync lulu
