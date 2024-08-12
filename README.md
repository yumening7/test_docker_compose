#### 构建db文件
```commandline
docker-compose run web python manage.py migrate
```

#### 启动docker
```commandline
docker-compose up --build
```