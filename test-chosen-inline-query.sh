curl -v -k -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache"  -d '{
"update_id":10000,
"chosen_inline_result":{
  "result_id": "12",
  "from":{
     "last_name":"Test Lastname",
     "type": "private",
     "id":1111111,
     "first_name":"Test Firstname",
     "username":"Testusername"
  },
  "query": "inline query",
  "inline_message_id": "1234csdbsk4839"
}
}' "http://localhost:5000/incoming"
