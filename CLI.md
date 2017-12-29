# Instructions for using the CLI
 
## `$ fbspider`

## When starting the program for the first time, use: `$ fbspider initialise`

#### This will ask for your graph ACCESS TOKEN, which you can find [here](https://developers.facebook.com/tools/accesstoken/)

## You can see your saved values by : `$ fbspider show [OPTIONS]`

```
Options:
  --token  Shows the user access token stored.
  --npa    Shows the default no of pages for given input.
  --npo    Shows the default no of top post in the output.
  --help   Show this message and exit.

```

## To edit these values, use : `$ fbspider edit [OPTIONS]`

```
Options:
  --token  Edits the user access token stored.
  --npa    Edits the no of pages.
  --npo    Edits the no of top post.
  --help   Show this message and exit.
  
```

## To search for a page, use : `$ fbspider search [OPTIONS] <Page name>`

```
Options:
  --npa INTEGER  the no of pages.
  --npo INTEGER  the no of top post.
  --help         Show this message and exit.
  
```

## To see the help message, use: `$ fbspider --help`

```
Usage: fbspider [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  edit        edits the specified value stored.
  initialise  Initialise with the required info.
  search      Search the page.
  show        Shows the specified value stored.
```
