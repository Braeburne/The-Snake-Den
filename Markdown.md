# Nick's Guide to Markdown ✒️

I'm lazy and don't want to keep referencing the internet for markdown syntax. Why not just throw all that stuff here in the repo? Yes, I like that idea.

What's great about this too is that you can see both sides - you can see the actual markdown code, and the output it generates in the "preview" or when reading the markdown page output like a regular web page.

## **Headers**
# # - Header 1
## ## - Header 2
### ### - Header 3
#### #### - Header 4
###### ##### - Header 5
###### ###### - Header 6

## **Text Formatting**
\**[text]** gives us **bold text.**

\__[text]__ also gives us __bold text.__

\*[text]* gives us *italicized text.*

\_[text]_ also gives us _italicized text._

The \<ins> tag in front of [text] gives us <ins> underlined text.

The "\\" escape character lets us intentionally break / prevent the text formatting operators from working, like this: "\\\<ins> [text]." 


## Body Formatting
To make this easier on ourselves, any instructions I give on body formatting will be bolded. Any other text is sample text for demonstration. 

**If you want to separate bodies of text from each other, likely with a newline character - understood traditionally as a space in normal people talk... then, simply insert one. Like this.**

"The Devil went down to Georgia
He was lookin' for a soul to steal
He was in a bind 'cause he was way behind
And he was willing to make a deal"

"When he came across this young man

Sawin' on a fiddle and playin' it hot

And the Devil jumped up on a hickory stump

And said 'Boy, let me tell you what' "

**From what I can tell, it's not possible to have two bodies of text be only one newline character apart from one another. It's always two. There's always that space between the lines, I can't figure out how to get lines under each other.**

**Hyphens "-" allow you to put bullet points in front of text, like this.**
- "text."
  
**You can also have multiple layers to the bullet points using tab indentation, like this:**

- "layer 1"
  - "layer 2"
    - "layer 3"
      - "layer 4, etc."

**The same thing works with numbered lists.**

1. L
2. I
3. S
4. T
5. "Layer 1"
   1. "Layer 2"
      1. Layer 3"
         1. "Layer 4"

**If you'd like to create what could be traditionally called a "quote," use the ">" chevron before a body of text. Like this.**

> NARRATOR: (Black screen with text; The sound of buzzing bees can be heard) According to all known laws
of aviation, there is no way a bee should be able to fly. Its wings are too small to get
its fat little body off the ground. The bee, of course, flies anyway because bees don't care
what humans think is impossible.

> BARRY BENSON: (Barry is picking out a shirt)
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.

> JANET BENSON: Barry! Breakfast is ready!

> BARRY: Coming! Hang on a second. (Barry uses his antenna like a phone) Hello?

> ADAM FLAYMAN: (Through phone) Barry?

> BARRY: Adam?

> ADAM: Can you believe this is happening?

> BARRY: I can't. I'll pick you up. (Barry flies down the stairs)

> MARTIN BENSON:
Looking sharp.

**If you would like text instead to be inside of what is traditionally a code block, surrounding the body of text with three "back tick" characters, ```.**

```
good ship,
lollipop
sweety trip,
candy... shoppu.
```

Apparently, indenting a line of text [x] times has the same effect as well.

    And I say,
    hey ye yaae yae yaa,
    hey ye yaae yaae
    I said hey!
    What's going on?
        And I say,
            hey ye yaae yae yaa,
                hey ye yaae yaae
                    I said hey!
                    What's going ooooon?
                                    [Spoken] AND HE TRIES

    oh my god do I try
        I try all the time,
    in this institution

Now this text copied straight from my Hash.md file is a strange case.




**Actual code can be formatted with that language's syntax highlighting if you specify the short-hand name of that language right after the first set of backticks. For example, Python code can be identified as follows:**

\`\`\`python

[your code here]

\`\`\`

## Misc. Formatting

If you want to create a link, this is how you do it. [Google](https://www.google.com/)

If you want to insert images, just as I have done previously on this page, you can do so by doing this. ![alt text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzdzYnF4dXJuZGx5MW52MGh3cHI4MnNlNTcyMWZyaDUzbDl5NTVrdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/as521kub4b68hW2JhK/giphy.webp "Alt Text Gang Baby.")

Or like this. 

![](https://media1.tenor.com/m/OzJRAe3gx-sAAAAC/ok-good.gif)