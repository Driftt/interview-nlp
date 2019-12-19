The database contains a table `chat_data`, with the following structure.

```
Table name:  chat_data
+----------------+---------------+------+-----+---------+
| Field          | Type          | Null | Key | Default |
+----------------+---------------+------+-----+---------+
| id             | int(11)       | NO   | PRI | NULL    | <-- unique ID for each row of data in a log.
| log_id         | int(11)       | YES  | MUL | NULL    | <-- refers to id in the logs table (conversation id).
| project_id     | int(11)       | YES  | MUL | NULL    | <-- refers to id in the projects table (corpus id).
| line           | int(11)       | YES  |     | NULL    | <-- line number in a log, starting at 1.
| time           | int(11)       | YES  |     | NULL    | <-- timestamp for a log row.
| data           | varchar(1024) | YES  |     | NULL    | <-- json encoded data.
+----------------+---------------+------+---------------+
```

This datbase contains data from chats between customers and agents. 

Data for each row of `chat_data` is encoded as JSON. Each JSON object contains keys for the actor, utterance, verb, and type.

`type` has the possible values `physical`, `spatial`, or `speech`.

`utterance` is only non-null when the type is `speech`.

`verb` is only non-null when the type is `physical`. These are things like button clicks, and indicate a non-linguistic user input.

`actor` is one of `agent` or `customer`.

Here is an example of a `data` dictionary:

```

{
  "actor": "customer",
  "verb": null,
  "type": "speech",
  "utterance": "Thanks for chatting with us!",
}
 
```
