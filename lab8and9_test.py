curl -s -X GET -H 'Accept: application/json' http://localhost:8080/containers

    resp = 'ok'
    return Response(response=resp, mimetype="application/json")
