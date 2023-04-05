# flask-locust-test
 Load testing simulator to understand how the monitoring, test system, and load generator work.
 

### Default auth for Grafana &amp; InfluxDB:

user: admin 

pass: admin123

### Default ports:

Grafana - 3000

InfluxDB - 8086

Chronograph - 8888

I was running all on wsl2 environment.

# Set up &amp; run the container
```
docker-compose up -d
```

# To stop the container
```
docker-compose down
```

# Grafana automatically set up containers monitoring dashboard

![grafana-dashboard-example](https://user-images.githubusercontent.com/47638863/230049894-09e6d30a-fd38-43d1-bc69-14660581cf3a.png)
