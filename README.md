# strf_hint

Are you confused when need to pass the encoded datatime format to function like `strfprint`? The specific
format coding can be tough to remember, due to a infrequent need to use it. Strf_hint can solve this trivial problem.

**Strf_hint** is lightweight and easy to use package, responsible for encoding the datatime formats using strf codes.

## Installation
TBD

## How to use it?
In order to transform custom datetime format into strf-codes-containing format, follow steps below:
```python
>>> from strf_hint.recognizer import Recognizer
>>> r = Recognizer()
>>> r.encode_format("Day: Sunday, 2022-Nov-30, 9:30 PM")
'format TBD'

```


## Contribution
In case of any bugs found or ideas feel free to contribute this repository. Issues and PR are welcome.

## License
[MIT LICENSE](https://opensource.org/license/mit/)
