# gpt3
Shell script gpt-3 helper

No complications. No nothing.
Export your API key to the variable OPENAI_API_KEY

You also may want to add the python script to your path so it is always available.

I also add a function to my bashrc:

```shell
function gpt3() {
  python3 -m gpt3 "$1"
}
```
