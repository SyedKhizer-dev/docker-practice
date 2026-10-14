# To access data stored in volume in the terminal:-
docker compose -f mongo.yaml exec mongo mongosh -u "khizer-db" -p "password123" --authenticationDatabase admin 

# If the containers are removed/deleted it has to be composed before viewing the data from terminal