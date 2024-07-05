# strf_hint

Are you confused when you need to pass the encoded datetime format to a function like strftime? 
The specific format codes can be tough to remember due to the infrequent need to use them. Strf_hint can solve this trivial problem.

**Strf_hint** is lightweight and easy to use package, responsible for encoding the datatime formats using strf codes.

## How to use it?
In order to transform custom datetime format into strf-codes-containing format, follow steps below:

```python
>>> from strf_hint.recognizer import Recognizer
>>> r = Recognizer()
>>> r.encode_format("Day: Sunday, 2022-Nov-30, 9:30 PM")
'Day: %A, %Y-%b-%d, %-I:%M %p'
```


## Contribution
In case of any bugs found or ideas feel free to contribute to this repository. Issues and PR are welcome.

## License
[MIT LICENSE](https://opensource.org/license/mit/)
