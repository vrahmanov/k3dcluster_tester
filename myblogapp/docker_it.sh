 docker build -t myapp .
 docker tag myapp localhost:5111/myapp
 docker push localhost:5111/myapp 
 kubectl run mynginx --image k3d-reg.localhost:5111/myapp