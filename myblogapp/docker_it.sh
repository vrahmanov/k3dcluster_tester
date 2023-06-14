 docker build -t myapp:blue .
 docker tag myapp:blue k3d-reg.localhost:5111/myapp:blue
 docker push k3d-reg.localhost:5111/myapp:blue 
 kubectl run mynginx --image k3d-reg.localhost:5111/myapp:blue