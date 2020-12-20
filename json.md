```
import json
```

```
>>> d = {'a': 1, 'b': 2}
>>> json.dumps(d)
'{"a": 1, "b": 2}'
```

Format
```
>>> json.dumps(d, separators=(',', ':'))
'{"a":1,"b":2}'
```
