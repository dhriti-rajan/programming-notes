def generate_header(title):
    header = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>""" + title + """</title>
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
<h1 class="title">""" + title + """
  <img src="https://lh3.googleusercontent.com/--c8480byC9k/AAAAAAAAAAI/AAAAAAAAAJo/SP9LwTne7mA/s46-c-k-no/photo.jpg"
       alt="notes">
</h1>
"""
    return header


def generate_footer():
    footer = """
<p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
         src="http://jigsaw.w3.org/css-validator/images/vcss"
         alt="Valid CSS!" />
  </a>
</p>
</body>
</html>
"""
    return footer


def extract_title(text):
    start = text.find('TITLE: ') + 7
    end = text.find('\n', start)
    return text[start:end]


def generate_subtopic(subtopic):
    output = ''
    output += '<div class="subtopic">'

    end = subtopic.find('\n')
    title = subtopic[:end]
    output += '<h4 class="topic">' + title
    output += '<a href="#" class="right">Back to Top &circ;</a></h4>\n'

    output += '<div class="content">' + subtopic[end:] + '</div>'
    output += '</div>\n'

    return output


def generate_topic(topic):
    output = ''
    output += '<div class="topic">'

    end = topic.find('\n')
    title = topic[:end]
    output += '<h3 class="topic">' + title
    output += '<a href="#" class="right">Back to Top &circ;</a></h3>\n'

    subtopics = topic.split('\nSUBTOPIC: ')
    for subtopic in subtopics[1:]:
        output += generate_subtopic(subtopic)
        generate_subtopic(subtopic)

    output += '</div>\n'
    return output


def generate_lesson(lesson):
    start = lesson.find('Lesson: ') + 8
    end = lesson.find('\n', start)
    title = lesson[start:end]

    output = ''
    output += '<div class="lesson">\n'
    output += '<h2 class="lesson">' + title
    output += '<a href="#" class="right">Back to Top &circ;</a></h2>\n'

    topics = lesson.split('\nTOPIC: ')
    for topic in topics[1:]:
        output += generate_topic(topic)

    output += '</div>\n'
    return output


def generate_all(input):
    lessons = input.split('LESSON: ')
    title = extract_title(lessons[0])

    output = ''
    header = generate_header(title)
    output += header

    for lesson in lessons[1:]:
        output += generate_lesson(lesson)

    footer = generate_footer()
    output += footer

    return output


def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


TEST_TEXT = """
TITLE: Udacity Programming Notes

LESSON: Lesson 1: The Basics of the Web and HTML

TOPIC: 1.1 The Basics of the Web and HTML

SUBTOPIC: Introduction to the Web
Topics covered:
<ul>
    <li>the web (what it is, what it looks like, how its major pieces fit together)
    </li>
    <li>HTML (main document type of the web)
    </li>
    <li>URL's (how you refer to documents on the web)
    </li>
    <li>HTTP (the protocol that unites the web/that the web runs on)
    </li>
    <li>web applications (what they are, how they fit into this big picture, grand finale, what the course is about)
    </li>
</ul>

SUBTOPIC: World-wide Web
World-wide Web:
<ul>
    <li>a collection of HTML documents
    </li>
    <li>these documents made of HTML (HyperText Markup Language)
    </li>
    <li>basis for almost every web page
    </li>
    <li>HTML = glues everything together
    </li>
    <li>World-wide web = invented in early 1990's
    </li>
</ul>

SUBTOPIC: Components of the Web
<ul>
    <li>you
    </li>
    <li>your computer running a browser
    </li>
    <li>internet
    </li>
    <li>servers (computers for sitting in a closet hosting files that make up the web rather than sitting on your desk browsing these files)
    </li>
</ul>

SUBTOPIC: HTML Basics
HTML is made up of:
<ul>
    <li>text content (what you see)
    </li>
    <li>markup (what it looks like)
    </li>
    <li>references to other documents (images, videos, etc.)
    </li>
    <li>links to other pages
    </li>
</ul>

SUBTOPIC: HTML Playground
<ul>
    <li>plain text = plain text in HTML for the most part
    </li>
    <li>to make text use different, we need to use markup
    </li>
</ul>

SUBTOPIC: HTML Tags
HTML Markup
<ul>
    <li>made up of things called tags
    </li>
    <li>example of tag: &lt;name&gt;contents&lt;/name&gt;
    </li>
    <ul>
        <li>&lt;name&gt; = opening tag
        </li>
        <li>&lt;/name&gt; = closing tag
        </li>
    </ul>
    <li>structure of tag:
    </li>
    <ul>
        <li>&lt;tag name&gt;tag contents&lt;/tag name&gt;
        </li>
        <li>whole tag = element
        </li>
    </ul>
</ul>

SUBTOPIC: Bold Tag
<ul>
    <li>structure of bold tag:
    </li>
    <ul>
        <li>&lt;b&gt;contents&lt;/b&gt;
        </li>
        <li>b = bold
        </li>
    </ul>
</ul>

SUBTOPIC: Italics
<ul>
    <li>structure of italic tag = same as bold tag
    </li>
    <ul>
        <li>em = emphasis
        </li>
        <li>&lt;em&gt;contents&lt;/em&gt;
        </li>
    </ul>
</ul>

SUBTOPIC: [ND] Computers Are Stupid
<ul>
    <li>when programmers say that computers are stupid, they are usually addressing an important point about how computers understand the instructions that human programmers give them
    </li>
    <li>think about how sensitive computers are to typos and how small mistakes (mistakes that a "smart" human could easily correct) can lead to huge problems when given to a "stupid" computer.
    </li>
</ul>

SUBTOPIC: Missing End Tag
<ul>
    <li>if an end tag is missing, the command applies to everything after the opening tag
    </li>
    <li>example:
    </li>
    <ul>
        <li>(correct) Dhriti&lt;em&gt;loves&lt;/em&gt; mysore pak = Dhriti <em>loves</em> mysore pak
        </li>
        <li>(incorrect) Dhriti&lt;em&gt;loves mysore pak = Dhriti <em>loves mysore pak</em>
        </li>
    </ul>
</ul>

SUBTOPIC: [ND] Scratchpad Warning
<ul>
    <li>learn how to connect the HTML documents you write to any other document on the internet by adding links
    </li>
</ul>

SUBTOPIC: Making Links
<ul>
    <li>HTML Attributes
    </li>
    <li>example:
    </li>
    <ul>
        <li>&lt;tag attr="value"&gt;contents&lt;/tag&gt;
        </li>
    </ul>
    <li>similarities:opening tag, end tag, content
    </li>
    <li>differences:attribute
    </li>
    <li>tags can have multiple attributes
    </li>
    <li>example:
    </li>
    <ul>
        <li>anchor tag, anchor = a
        </li>
        <li>&lt;a href="www.reddit.com"&gt;derp&lt;/a&gt;
        </li>
        <li>derp = content
        </li>
        <li>href = attribute name
        </li>
        <li>www.reddit.com = value
        </li>
        <li>anchor tag makes things links rather than normal text
        </li>
    </ul>
</ul>

SUBTOPIC: Adding Images
<ul>
    <li>image tag structure:
    </li>
    <ul>
        <li>&lt;img src="url" alt="text"&gt;
        </li>
        <li>image tag = void tag (no content, so no end tag necessary)
        </li>
    </ul>
</ul>

SUBTOPIC: Whitespace
<ul>
    <li>if you enter text in multiple lines, it shows up as one long line unless you use the line break tag (void tag)
    </li>
    <li>example:
    </li>
    <ul>
        <li>Dhriti &lt;br&gt;loves&lt;br&gt; mysore pak = Dhriti<br> loves<br> mysore pak
        </li>
    </ul>
    <li>other option = paragraph tag
    </li>
    <li>structure = &lt;p&gt;content&lt;/p&gt;
    </li>
</ul>

SUBTOPIC: Inline vs Block
<ul>
    <li>why do we have a break tag and a paragraph tag?
    </li>
    <li>break = inline (just text)
    </li>
    <li>paragraph = block (makes imaginary box with height and width)
    </li>
</ul>

SUBTOPIC: [ND] Where to Focus
<ul>
    <li>container elements - elements that do nothing but contain stuff inside themselves
    </li>
</ul>

SUBTOPIC: Span and Div
<ul>
    <li>&lt;span&gt;content&lt;/span&gt;
    </li>
    <li>&lt;div&gt;content&lt;/div&gt;
    </li>
    <li>differences:
    </li>
    <ul>
        <li>span = inline
        </li>
        <li>div = block
        </li>
    </ul>
    <li>function:contain content
    </li>
    <li>possibilities:attach styles/adjust different behaviors of how they display
    </li>
    <li>examples:
    </li>
    <ul>
        <li>&lt;span class="foo"&gt;content&lt;/span&gt;
        </li>
        <li>&lt;div class="bar"&gt;content&lt;/div&gt;
        </li>
    </ul>
    <li>inline elements:
    </li>
    <ul>
        <li>a, span, br, img, strong
        </li>
    </ul>
    <li>block elements:
    </li>
    <ul>
        <li>div, p, form
        </li>
    </ul>
</ul>

SUBTOPIC: Document Structure
                COMPLETE HTML DOCUMENT:
                &lt;!DOCTYPE HTML&gt; - doctype
                - &lt;html&gt;
                -- &lt;head&gt;
                &lt;title&gt;Title!&lt;/title&gt; - title
- &lt;/head&gt;
--- &lt;body&gt;
&lt;b&gt;content&lt;/b&gt;
--- &lt;/body&gt;
- &lt;/html&gt;
<ul>
    <li>head contains metadata, Javascript, CSS (filing)
    </li>
    <li>body = content of document
    </li>
                HTML Document (different view)
                red = focus
                &lt;head&gt;
                title CSS JS
                &lt;/head&gt;
                &lt;body&gt;
                contents
                &lt;/body&gt;
    <li>we will focus on generating the body section of an HTML document
    </li>
</ul>

SUBTOPIC: [ND] Think About What You've Learned
<ul>
    <li>two main topics = overview of internet, introduction to HTML
    </li>
    <li>overview of internet:big-picture view of how the internet works/servers, browsers, internet, HTTP
    </li>
    <li>introduction to HTML: HTML (tags&lt;b&gt;, &lt;p&gt;, &lt;em&gt;) even though these tags aren't visible to users of a web page, they still carry meaning that is meaningful to web browsers
    </li>
    <li>(What a Web Page Is) a web page is a text document written in a language called HTML. Web browsers read these documents, and then interpret and display them
    </li>
    <li>(How Coding Works) coding happens when programmers write text in a language that a computer can understand so that computer can then follow the instructions the programmer wrote
    </li>
    <li>(Computers Are Stupid) programmers need to write exactly the way a computer understands (also known as writing with correct "syntax")
    </li>
    <li>(Basic HTML Vocabulary):
    </li>
    <ul>
        <li>Tag: An HTML tag is always contained within angled brackets. Most tags have an opening tag (&lt;p&gt; for example) and a closing tag, (&lt;/p&gt;). Some tags (called "void" tags) do not require a closing tag (like the &lt;br&gt; tag).
        </li>
        <li>Element: An HTML element refers to everything within a set of opening and closing tags.
        </li>
        <li>Attribute: This is a property of an HTML element. For example, to set the href attribute of an anchor tag to the Udacity URL, you would write&lt;a href="www.udacity.com"&gt;Udacity&lt;/a&gt;
        </li>
    </ul>
</ul>

TOPIC: 1.2 Creating a Structured Document

SUBTOPIC: The First Step
<ul>
    <li>html = structure
    </li>
    <li>css = styling
    </li>
    <li>javascript = interactive components
    </li>
</ul>

SUBTOPIC: Exploring the Web
<ul>
    <li>If you go to a wikipedia page and go to developer tools, you can read the same text as there is on the page when you go deep enough
    </li>
    <li>all of the elements you can see are rectangular
    </li>
    <li>you cannot see all of the elements
    </li>
Page Structure
    <li>Sideways triangles are an html element
    </li>
    <li>tree-like structure
    </li>
</ul>

SUBTOPIC: [ND] Focus Checkpoint
<ul>
    <li>HTML and CSS are both "languages"
    </li>
    <li>HTML controls the "structure" of a web page
    </li>
    <li>CSS controls the "style" of a page (how it looks)
    </li>
    <li>When programmers talk about the "DOM" (Document Object Model) they are talking about the tree-like structure of a page
    </li>
</ul>

SUBTOPIC: HTML-CSS-DOM
<ul>
    <li>HTML = language-syntax+rules
    </li>
    <li>HTML/DOM = tag-elements in a tree
    </li>
    <li>CSS = use syntax + rules to change how elements look on a page (font size, color, background)
    </li>
</ul>

SUBTOPIC: Boxes Everywhere
<ul>
    <li>everything in web pages is made of rectangles (a box)
    </li>
    <li>when you have circles and you uncheck border radius, the circles become squares
    </li>
</ul>

SUBTOPIC: Boxes, Grids, and Rules
<ul>
    <li>Thinking of objects on a web page as boxes makes things a lot easier
    </li>
    <li>using boxes, we can easily rearrange them to give users a different experience
    </li>
</ul>

SUBTOPIC: [ND] How to Listen to Experts
<ul>
    <li>Experts will:
    </li>
    <li>assume you have knowledge that you don't
    </li>
    <li>use jargon you don't understand
    </li>
    <li>speak too quickly for you to understand
    </li>
</ul>

SUBTOPIC: Interview with Jacques
<ul>
    <li>how to approach a new design
    </li>
    <li>make boxes by drawing with pencil
    </li>
</ul>

SUBTOPIC: Boxes to HTML
<ul>
    <li>How to make a box into html:
    </li>
    <ul>
        <li>define boxes with div tags
        </li>
    </ul>
    <li>to apply style, we need to label each element, or give each element a class attribute
    </li>
    <li>elements can have multiple classes
    </li>
    <li>make sure you give class names that make sense
    </li>
Summaries:
We can make basic web pages in HTML and then add style to them by using CSS.
i.3 Adding CSS Style and HTML Structure
</ul>

SUBTOPIC: Where to Focus Your Attention
Don't repeat yourself in CSS

SUBTOPIC: Understanding CSS
<ul>
    <li>CSS = Cascading Style Sheets
    </li>
    <li>You can have several CSS files or sheets that will be referenced in HTML and all of them will be used to find out the final and visible style for your page
    </li>
    <li>Cascading - the most specific rule (the rule that best describes the elements) is applied to every element
    </li>
</ul>

SUBTOPIC: [ND] Thinking About "Cascading"
<ul>
    <li>Inheritance is a key feature in CSS
    </li>
    <li>Inheritance relies on the ancestor-descendant relationship to operate
    </li>
    <li>Inheritance - the mechanism by which properties are applied not only to a specific element, but also to its descendants
    </li>
    <li>box-related properties are not inherited
    </li>
    <li>properties that can be inherited: color, font, letter-spacing, line-height, list-style, text-align, text-indent, text-transform, visibility, white-space, and word-spacing
    </li>
    <li>properties that can't be inherited: background, border, display, float and clear, height and width, margin, min- and max-height and -width, outline, overflow, padding, position, text-decoration, vertical-align, and z-index
    </li>
    <li>Inheritance prevents repetition in a style sheet, so it is easier to write
    </li>
    <li>inheritance enhances faster-loading of web pages by users and enables the clients to save bandwidth and development costs
    </li>
    <li>descendant elements inherit text-related properties
    </li>
    <li>descendant elements may inherit CSS property values from any ancestor element enclosing them
    </li>
    <li>inheritance relies on the document tree, which is the hierarchy of (X) HTML elements in a page based on nesting
    </li>
</ul>

SUBTOPIC: Styling Up
<ul>
    <li>in CSS, you first write a selector, which defines what elements of a page a particular style will apply to
    </li>
    <li>you can select an HTML tag, and that rule will apply to all tags on the page
    </li>
    <li>to apply a style to all paragraphs on a page you can write:
    </li>
    <ul>
        <li>p {
        </li>
                                }
    </ul>
    <li>or,
    </li>
    <ul>
        <li>select elements by class
        </li>
        <li>ex. (apply style to class description)
        </li>
        <li>.description {
        </li>
                                color: red; (attribute: value;)
                                }
    </ul>
    <li>or,
    </li>
    <ul>
        <li>combine selectors (ex.select all links inside an element with class article)
        </li>
    </ul>
</ul>

SUBTOPIC: Using Semantic Tags
<ul>
    <li>Changing the visual properties of an element only changes how the element is displayed, not what kind of element it is
    </li>
    <li>you should choose the right type of element for a certain part of a page depending on the purpose of that element
    </li>
    <li>you can have multiple headings in HTML (h1, h2, h3, etc.)
    </li>
    <li>search engines also use headings to index the structure and content of a web page
    </li>
</ul>

SUBTOPIC: The Box Revisited
<ul>
    <li>the box model:
    </li>
    <ul>
        <li>margin
        </li>
        <li>border
        </li>
        <li>padding
        </li>
        <li>content
        </li>
        <li>padding
        </li>
        <li>border
        </li>
        <li>margin
        </li>
    </ul>
    <li>we can change the heights and widths of these boxes
    </li>
    <li>the size of the element is the sum of the widths of the border, padding, and content
    </li>
    <li>to see size of box, type:
    </li>
    <ul>
        <li>*{
        </li>
                                        box-sizing: border-box;
                                }
    </ul>
    <li>we can set the box size in either pixels or percentage
    </li>
    <li>we can set a max width for the box
    </li>
    <li>when you add the border-box definition and max-width attributes, the box sizes are different, but the layout stays the same
    </li>
    <li>flex box layout: flex box means flexible box and it provides an efficient way to lay out, align, and distribute space among items in a container, or, div
    </li>
    <li>if you want several elements next to each other, you can change the display attribute of the parent container to value flex
    </li>
    <ul>
        <li>for this to work, you must give the items a size that is smaller than the default 100%
        </li>
    </ul>
</ul>

SUBTOPIC: [ND] Box Sizing and Positioning Summary
Box Sizing
There are four main points that Jessica addressed about box sizing.
<ol>
    <li>HTML elements are boxes and each box has 4 components.
    </li>
    <li>Because there are so many components to each box, it can often be hard to get the size of a box just right.
    </li>
    <li>There are two techniques you can use to help deal with sizing issues.
    </li>
    <ol>
        <li>Set sizes in terms of percentages rather than pixels.
        </li>
        <li>Set the box-sizing attribute to border-box for every element.
        </li>
    </ol>
    <li>Different browsers work slightly differently. Sometimes this causes different browsers to display the same code differently.
    </li>
</ol>

Box Positioning
<ol>
    <li>Divs are block elements (as opposed to inline), so by default they take up the entire width of a page.
    </li>
    <li>Adding the rule display: flex; to the appropriate CSS will override this behavior and let divs appear next to each other.
    </li>
</ol>

SUBTOPIC: Code, Test, Refine
<ol>
    <li>Look for natural boxes
    </li>
    <li>Look for repeated styles and semantic elements
    </li>
    <li>write your HTML
    </li>
    <li>apply your styles
    </li>
    <li>fix the small things
    </li>
    <li>using developer tools, you can test things on the fly and see how it affects your page without changing the HTML and CSS files.
    </li>
</ol>

LESSON: Lesson 2: Automate Your Page

TOPIC: 2.1 Introduction to Serious Programing

SUBTOPIC: Introduction
<ul>
    <li>course will:
    </li>
    <ul>
        <li>introduce you to fundamental ideas in computing
        </li>
        <li>teach you to read and write your own computer programs
        </li>
        <li>we will do this in the context of building a search engine (google, bing, etc.)
        </li>
        <li>search engine:
        </li>
        <ul>
            <li>if you type in what you are looking for, the results come back very fast
            </li>
        </ul>
        <li>class goal:
        </li>
        <ul>
            <li>turn some of the magic of a search engine into something a bit more understandable
            </li>
        </ul>
        <li>largest class goal:
        </li>
        <ul>
            <li>learn about computer science
            </li>
        </ul>
        <li>computer science is about how to solve problems like building a search engine by breaking them into smaller pieces and then precisely and mechanically describing a sequence of steps that you can use to solve each piece
        </li>
        <ul>
            <li>these steps can be executed by a computer
            </li>
        </ul>
        <li>for building a search engine, the three main pieces are:
        </li>
        <ul>
            <li>finding data by crawling web pages
            </li>
            <li>building an index to be able to respond quickly to search queries
            </li>
            <li>ranking pages so that we get the best result for a given query
            </li>
        </ul>
        <li>during course, we won't cover everything you need to build a search engine as powerful as google, but we will cover the main ideas and learn a lot about computer science
        </li>
        <ul>
            <li>first three units:
            </li>
            <ul>
                <li>building the web crawler
                </li>
            </ul>
            <li>units 4 & 5:
            </li>
            <ul>
                <li>how to respond to queries quickly
                </li>
            </ul>
            <li>unit 6:
            </li>
            <ul>
                <li>how to rank results and cover the method Google uses to rank pages, that made it so successful
                </li>
            </ul>
            <li>first we will talk about how to make a web crawler that we are going to use to get data for our search engine
            </li>
        </ul>
    </ul>
</ul>

SUBTOPIC: Advice from Sergey Brin
<ul>
    <li>most important thing in building a search engine:
    </li>
    <ul>
        <li>have a good, fun corpus to start with (ex. world-wide web)
        </li>
    </ul>
</ul>

SUBTOPIC: Overview of the Unit
<ul>
    <li>the goal of the first three units in this course is to build a web crawler that will collect data from the web for our search engine, and to learn about big ideas in computing by doing that
    </li>
    <li>in unit 1, we will get started by extracting the first link on a web page
    </li>
    <ul>
        <li>a web crawler finds web pages for our search engine by starting from a "seed" page and following links on that page to find other pages
        </li>
        <li>each of those links leads to some new web page, which itself could have links that lead to other pages
        </li>
        <li>as we follow those links, we will have more and more web pages, building a collection of data that we will use for our search engine
        </li>
    </ul>
    <li>a web page is a chunk of text that comes from the internet into your web browser
    </li>
    <ul>
        <li>a link is just a special type of text in that web page
        </li>
        <li>when you click on a link in your browser, it will direct you to a new page
        </li>
    </ul>
    <li>what we will do in this unit is write a program to extract that first link from the web page
    </li>
    <li>in later units, we will figure out how to extract all of the links and build their collection for our search engine
    </li>
    <li>a computer is a machine that can be programmed
    </li>
</ul>

SUBTOPIC: What is Programming?
<ul>
    <li>programming is the core to computer science
    </li>
    <li>most machines are only designed to do one thing only
    </li>
    <li>without a program, a computer is less useful than a toaster
    </li>
    <ul>
        <li>the program is what tells the computer what to do
        </li>
        <li>the power of a computer, is that, unlike a toaster, which is only designed to do a few things, a computer can do anything
        </li>
        <li>a computer is a universal machine, and we can program it to do essentially any computation
        </li>
        <li>anything that we can imagine and figure out how to write a program for, we can make the computer do
        </li>
        <li>a program needs to be a very precise sequence of steps
        </li>
        <li>a computer without a program barely knows how to do anything, but it has a few simple instructions that it can execute
        </li>
        <ul>
            <li>to make a program useful, we need to put those instructions together in a way that it does what we want
            </li>
        </ul>
        <li>a computer can to any computation we want it to do
        </li>
        <ul>
            <li>the power of a computer is that it can execute these steps very fast
            </li>
            <li>we can execute billions of instructions in one second
            </li>
            <li>the program gives us a way to tell the computer what steps to take
            </li>
        </ul>
    </ul>
    <li>there are many different languages for programming computers
    </li>
    <li>we will learn how to use python in this course
    </li>
    <li>python is named after Monty Python
    </li>
    <li>the important thing about python is that it gives us a nice, high-level language that we can use to write programs
    </li>
    <ul>
        <li>this means that instead of our program running directly on the computer, the programs we write will be an input to the Python program which runs on the computer
        </li>
        <li>python is an interpreter
        </li>
        <li>this means that it runs our programs, interprets them, executes the programs that we wrote in Python language by running a program in a language that the computer can understand directly
        </li>
    </ul>
</ul>

SUBTOPIC: Getting Started With Python
<ul>
    <li>Print is the python command that prints something out
    </li>
    <ul>
        <li>after the print we have an expression and the value of that expression is what gets printed
        </li>
        <ul>
            <li>this can be simple, like the number three, but it can also be a more complicated expression, such as doing some arithmetic
            </li>
        </ul>
    </ul>
    <li>IDE's have an environment, where the code is edited, as well as a place to see what your code produces
    </li>
</ul>

SUBTOPIC: Language Ambiguity
<ul>
    <li>why do we need to invent new languages like Python to program computers, rather than using natural languages?
    </li>
    <ul>
        <li>ambiguity (english words can have multiple meanings, but we need the computer to only interpret the correct meaning of the program)
        </li>
        <li>verbosity (normal languages would need too much text)
        </li>
    </ul>
</ul>

SUBTOPIC: Grammar
<ul>
    <li>programming languages take things very literally
    </li>
</ul>

SUBTOPIC: Backus-Naur Form
<ul>
    <li>the purpose of Backus-Naur form is to be able to precisely describe exactly the language in a way that is very simple and very concise
    </li>
    <li>each rule has this form:
    </li>
    <ul>
        <li>&lt;Non-terminal&gt; (something we are not finished with) &rarr; replacement (can be anything (sequence of non-terminals, one non-terminal, terminal))
        </li>
        <ul>
            <li>non-terminals are sometimes written inside brackets
            </li>
            <li>&lt;non-terminal&gt; &rarr; replacement
            </li>
        </ul>
        <li>terminals never appear on the left side of a rule
        </li>
        <li>we cannot replace terminals
        </li>
        <li>we keep replacing the non-terminals with their replacements until there are only terminals left
        </li>
        <li>we can form a sentence by starting from some non-terminal
        </li>
        <ul>
            <li>by following the rules, we keep replacing non-terminals with their replacements until we are left with only terminals
            </li>
            <li>we usually start with the non-terminal which is written in the top left
            </li>
        </ul>
    </ul>
    <li>derivation - starting from some non-terminal, follow the rules to derive a sequence of terminals
    </li>
    <ul>
        <li>we can derive a sentence in grammar
        </li>
    </ul>
</ul>

SUBTOPIC: Python Expressions
<ul>
    <li>python grammar is much stricter than english grammar
    </li>
    <ul>
        <li>in python, the code must match the language grammar exactly
        </li>
        <li>if some code you type is not grammatical, you get a syntax error
        </li>
    </ul>
    <li>we will start looking at python grammar by looking at a non-terminal expression
    </li>
    <li>an expression is something that has a value
    </li>
    <ul>
        <li>we can make an expression by combining two expressions with an operator
        </li>
        <ul>
            <li>this is sort of like the sentence rule we have for english where we could make a sentence by combining a subject, a verb, and an object
            </li>
            <ul>
                <li>this is a lot more interesting, though, because we have expressions on both the left side and the right side, so it looks kind of circular
                </li>
                <ul>
                    <li>because we have other rules, it is not completely circular
                    </li>
                    <ul>
                        <li>this is what is called a recursive definition
                        </li>
                    </ul>
                </ul>
            </ul>
            <li>part of python grammar:
            </li>
            <ul>
                <li>expression &rarr; expression operator expression
                </li>
                <li>expression &rarr; number
                </li>
                <li>expression &rarr; (expression)
                </li>
                <li>operator &rarr; +
                </li>
                <li>operator &rarr; *
                </li>
                <li>number &rarr; 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 . . .
                </li>
            </ul>
        </ul>
        <li>recursive grammar rules are very powerful
        </li>
        <li>we only need a few simple rules to describe a big language
        </li>
    </ul>
</ul>

SUBTOPIC: Speed of Light
<ul>
    <li>speed of light = 2997924458 meters per second
    </li>
    <li>meter = 100 centimeters
    </li>
    <li>nanosecond - one billionth of a second
    </li>
    <li>python does multiplication more accurately if you change the decimal point of a number (ex. 1 versus 1.0)
    </li>
</ul>

SUBTOPIC: Processors
<ul>
    <li>using "apple menu, about this mac" you can find out what type of processor you have
    </li>
    <li>GHC stands for gigahertz
    </li>
    <li>if we have the processor 2.7 GHZ Intel Core, we can do 2.7 billion cycles in one second
    </li>
    <li>the time that the computer has to do one step is a cycle
    </li>
    <li>in this case the computer has less than a nanosecond
    </li>
    <li>in the time that a computer has to do one cycle, light travels 11.1 centimeters
    </li>
</ul>

SUBTOPIC: Grace Hopper
<ul>
    <li>Admiral grace hopper was one of the pioneers in computing
    </li>
    <li>she was famous for carrying a nanostick
    </li>
    <ul>
        <li>a nanostick is a stick with the length of the distance that light travels in one nanosecond
        </li>
    </ul>
    <li>she was famous for writing one of the first languages
    </li>
    <ul>
        <li>she wrote COBOL
        </li>
        <li>COBOL was for a long time the most widely-used computer language
        </li>
    </ul>
    <li>she was one of the first people to think about writing languages this way
    </li>
    <li>quote from grace hopper:
    </li>
    <ul>
        <li>"Nobody believed that I had a running compiler and nobody would touch it.  They told me computers could only do arithmetic."
        </li>
        <ul>
            <li>a compiler is a program that produces other programs, like python
            </li>
            <li>the difference between a compiler and an interpreter like python is that the compiler does all the work at once and then runs the new program whereas with an interpreter like python, you're doing this work at the same time
            </li>
        </ul>
    </ul>
</ul>

TOPIC: Stage 2: Work Session 1

SUBTOPIC: Practice: Apply What You Learned
<ul>
    <li>debugging is one of the 5 ways that programmers think
    </li>
</ul>

SUBTOPIC: Before You Continue
<ul>
    <li>programming mistakes are called bugs
    </li>
</ul>

TOPIC: 2.2 Variables and Strings

SUBTOPIC: [ND] Where to Focus Your Attention
<ul>
    <li>one of the most important topics in programming is the variable
    </li>
</ul>

SUBTOPIC: Variables
<ul>
    <li>in python, we can use variables to create a name and use that name to refer to a variable
    </li>
    <li>the way to introduce a variable is to use an assignment statement
    </li>
    <ul>
        <li>assignment statement layout:
        </li>
        <ul>
            <li>name=expression
            </li>
            <ul>
                <li> the name refers to the value that the expression has
                </li>
                <li>the name can be any sequence of letters and numbers, as well as underscores, as long as it starts with a letter or underscore (ex.)
                </li>
                <li>speed_of_light=299792458
                </li>
                <li>the name speed_of_light refers to the value 299792458
                </li>
                <li>way to refer to this:
                </li>
                <li>speed_of_light &rarr; 299792458
                </li>
                <li>arrow means "refers to"
                </li>
            </ul>
            <li>once we are done with the assignment, we can use the name and the value of that name is the value that it refers to
            </li>
        </ul>
        <li>we can use variables to make our programs easier to understand, and to use the same expression multiple times
        </li>
        <li>we can write comments if we start with a hash symbol
        </li>
        <li>comments are not interpreted in python
        </li>
    </ul>
</ul>

SUBTOPIC: Variables can Vary
<ul>
    <li>we can change the value of a variable and the next time we use it, it will correspond to the new value
    </li>
    <li>we can use variables in their own assignment statements (ex.)
    </li>
    <ul>
        <li>days=days-1
        </li>
    </ul>
    <li>in python, equal signs mean assignments
    </li>
</ul>

SUBTOPIC: Strings
<ul>
    <li>in the early days of computing, people thought of computers as very powerful calculators
    </li>
    <li>they could simulate nuclear weapons
    </li>
    <li>they could compute ballistic tables
    </li>
    <li>they could break encryptions
    </li>
    <ul>
        <li>this was a little more than just arithmetic, but it was still mostly about counting doing simple arithmetic
        </li>
    </ul>
    <li>computers can operate on any kind of data we want
    </li>
    <li>this gets much more interesting when we operate on data besides just numbers
    </li>
    <li>if we are going to build a search engine, most of the data that we want to deal with is not numbers, but the letters that are contained in web pages, and in python these are called strings
    </li>
    <li>a string is just a sequence of characters surrounded by quotes
    </li>
    <li>we have to print strings or variables to make words, because if we do not have quotes around the words, it looks like a variable that we did not define
    </li>
    <li>we can use either double quotes or single quotes to surround a string, as long as we use the same type of quote to start the string as we do to end it
    </li>
</ul>

SUBTOPIC: Ada
<ul>
    <li>Augusta Ada King = "Countess of Lovelace"
    </li>
    <li>she is the world's first programmer
    </li>
    <li>in the 1840's, she started to think about how to program mechanical computers
    </li>
    <ul>
        <li>she was the first person to do this
        </li>
        <li>charles babbage was starting to build these (analytical engine)
        </li>
        <li>he never succeeded in building it because 1840's technology was not enough for building something that precise, but he had a design for it, and ada was thinking about programming it to do more interesting things
        </li>
        <li>grace hopper was not the first person to think about doing things other than arithmetic with computers
        </li>
        <ul>
            <li>ada was thinking about this in the 1840's
            </li>
        </ul>
    </ul>
</ul>

SUBTOPIC: Hello!!! Solution
<ul>
    <li>the value of a string + another string is concatenation
    </li>
    <ul>
        <li>this is a new string that is the result of pasting the two strings together
        </li>
        <li>concatenation does not immediately add spaces
        </li>
    </ul>
</ul>

SUBTOPIC: Strings and Numbers
<ul>
    <li>we cannot concatenate strings and numbers together
    </li>
    <li>we can multiply strings by numbers so that they repeat themselves
    </li>
</ul>

SUBTOPIC: Indexing Strings
<ul>
    <li>we can extract subsequences from the strings, but not numbers
    </li>
    <li>a string is a sequence of characters
    </li>
    <li>if we have a string, we can use square brackets to extract parts of that string
    </li>
    <ul>
        <li>example:
        </li>
        <li>"udacity"[2] = a
        </li>
        <li>in this case, we only select the 2nd character in the string
        </li>
        <li>we can also say:
        </li>
        <li>"udacity"[1+1] = a
        </li>
        <li>positive numbers count from left to right
        </li>
        <li>negative numbers count from right to left
        </li>
    </ul>
</ul>

SUBTOPIC: Selecting Sub-sequences
<ul>
    <li>indexing strings:
    </li>
    <ul>
        <li>&lt;string&gt;[&lt;expression&gt;]
        </li>
    </ul>
    <li>selecting a sub-sequence of the string:
    </li>
    <ul>
        <li>&lt;string&gt;[&lt;expression&gt;:&lt;expression&gt;]
        </li>
        <li>the sub-sequence starts at the first expression and ends at the second
        </li>
        <li>in all of these, the expression must equate to a number
        </li>
        <li>in sub-sequences, the selected characters are the first character stated to the one right before the second one stated
        </li>
    </ul>
</ul>

SUBTOPIC: Finding Strings Inside Strings
<ul>
    <li>the "Find" operation helps us find a small sub-string in a huge string
    </li>
    <li>Find is a method, or a built in procedure provided by python
    </li>
    <li>find is a procedure that operates on strings, so we use it by having a string followed by .find, followed by a parentheses, then we pass in another string (which is the string that we want to find in the huge string)
    </li>
    <ul>
        <li>&lt;string&gt;.find(&lt;string&gt;)
        </li>
    </ul>
    <li>the output of find is the position in the string where that sub-string is found, the first occurrence of the string
    </li>
    <ul>
        <li>if that string occurs in more than one place in the input string, the result of find will always give you the position, or the number where the first occurrence of the sub-string occurs
        </li>
    </ul>
    <li>the output of using find will be a number representing the first position in the search string, where the target string first occurs
    </li>
    <ul>
        <li>if the target string is not found anywhere in the search string, then the output would be negative 1
        </li>
        <li>for the position, the number is the number of the character in the search string that the target string starts from
        </li>
        <li>we can validate the number using string indexing
        </li>
        <li>the result of finding an empty string is always 0
        </li>
    </ul>
</ul>

SUBTOPIC: [ND] Focus Checkpoint
<ul>
    <li>parameters are what are inside the parentheses for find
    </li>
</ul>

SUBTOPIC: Finding with Numbers
<ul>
    <li>for find, we can add an extra parameter, which is a number
    </li>
    <ul>
        <li>normally find will find the first occurrence of the target string in the search string, but using the extra parameter (which is the number of a character in the search string), find will locate the first occurrence of the target string after the character with the number of the parameter
        </li>
        <ul>
            <li>if the extra parameter that you add is a number that is in the middle of one occurrence of the target string, the find output will be the occurrence after that
            </li>
            <li>&lt;string&gt;.find(&lt;string&gt;, &lt;number&gt;)
            </li>
        </ul>
    </ul>
</ul>

TOPIC: 2.3 Input->Function->Output

SUBTOPIC: [ND] Where You Left Off
<ul>
    <li>functions are one of the most important ideas in programming
    </li>
</ul>

SUBTOPIC: [ND] Where to Focus Your Attention
<ul>
    <li>we can make functions that, when given a little bit of text as input (maybe a name and a concept description), will automatically generate HTML
    </li>
</ul>

SUBTOPIC: Dave, Sebastian, and Junior
<ul>
    <li>taking data in is essential to making self driving cars work
    </li>
    <li>self driving cars have lots of sensors that take data in
    </li>
    <li>the sensors and cameras take data in and then funnel it back into the car so that it does not bump into anything when it is driving
    </li>
</ul>

SUBTOPIC: Using Procedures
<ul>
    <li>how to use a procedure
    </li>
    <li>a procedure is a function
    </li>
    <ul>
        <li>the inputs below are often called operands, or arguments
        </li>
        <li>&lt;procedure&gt;(&lt;input&gt;, &lt;input&gt;, . . . )
        </li>
        <li>find is similar since you use one or two inputs (the two strings)
        </li>
        <ul>
            <li>it is also different since the inputs are separate and it is built in, rather than you having to define it
            </li>
        </ul>
    </ul>
    <li>for the procedures that I will define myself, there will be no object to invoke them on
    </li>
    <li>the number of parameters in a def is the same as the number of inputs
    </li>
    <li>example:
    </li>
    <ul>
        <li>def rest_of_string(s):
        </li>
        <ul>
            <li>return s[1:]
            </li>
        </ul>
    </ul>
    <li>way to use this:
    </li>
    <ul>
        <li>print rest_of_string("hello")
        </li>
        <li>this will print: ello
        </li>
    </ul>
    <li>we must have return statements in defs, otherwise our output will be "none"
    </li>
</ul>

TOPIC: Stage 2: Work Session 3

SUBTOPIC: Practice: Apply What You Learned
<ul>
    <li>calling a function is the same as using a function
    </li>
</ul>

TOPIC: 2.4 Control Flow and Loops: If and While

SUBTOPIC: [ND] Where to Focus Your Attention
<ul>
    <li>if statements control which code gets executed when
    </li>
</ul>

SUBTOPIC: Equality Comparisons
<ul>
    <li>we can make code behave differently based on certain decisions
    </li>
    <li>Boolean Value
    </li>
    <ul>
        <li>true or false
        </li>
    </ul>
    <li>we can make comparisons of numbers
    </li>
    <ul>
        <li>&lt;number&gt;&lt;operator&gt;&lt;number&gt;
        </li>
        <li>!= is not equal to
        </li>
    </ul>
</ul>

SUBTOPIC: If Statements
        if &lt;test expression&gt;:
                &lt;block&gt;

SUBTOPIC: Or
<ul>
    <li>if we have multiple constraints we can use or, just like else
    </li>
    <li>&lt;expression&gt; or &lt;expression&gt;
    </li>
    <ul>
        <li>if the first expression evaluates to true, the value is true and the second expression is not evaluated.
        </li>
        <li>if the first expression evaluates to false, the value is the value of the second expression
        </li>
    </ul>
</ul>

SUBTOPIC: Biggest Solution
<ul>
    <li>we can define any of the built in procedures in python
    </li>
    <li>Alan Turing was the probably most important computer scientist
    </li>
    <li>in 1936 he developed an abstract model of a computer which we now know as the "Turing machine"
    </li>
    <li>he proved that a machine with a few simple operations could simulate any other machine
    </li>
    <li>in the 1930's, people thought a computer was a person who did calculations
    </li>
    <li>Alan Turing helped break the enigma code in Bletchley Park
    </li>
    <ul>
        <li>the enigma code was the most widely used cypher code by the Nazis
        </li>
        <li>Alan Turing built machines that could be used to break the Enigma code
        </li>
        <ul>
            <li>these machines were sort of like computers in that they did lots of calculations
            </li>
            <li>unlike computers, these machines were not programmable
            </li>
            <li>they could only do a specific calculation that was useful for breaking the code
            </li>
        </ul>
    </ul>
</ul>

SUBTOPIC: While Loops
<ul>
    <li>a loop is a way to do things over and over again
    </li>
    <li>while loop:
    </li>
    <ul>
        <li>while &lt;test expression&gt;:
        </li>
        <ul>
            <li>&lt;block&gt;
            </li>
        </ul>
    </ul>
    <li>the block is a set of instructions
    </li>
    <li>while loops are similar to the if statement
    </li>
</ul>

SUBTOPIC: Break Statement
<ul>
    <li>break is a way to stop the while loop after a while
    </li>
    <li>while &lt;test expression&gt;
    </li>
    <ul>
        <li>&lt;code&gt;
        </li>
        <li>if &lt;break test&gt;
        </li>
        <ul>
            <li>break
            </li>
        </ul>
        <li>&lt;more code&gt;
        </li>
    </ul>
    <li>&lt;after while&gt;
    </li>
</ul>

TOPIC: 2.5 Debugging

SUBTOPIC: Bugs Happen
<ul>
    <li>Maurice Wilkes invented the EDSAC, one of the world's first programmable computers
    </li>
</ul>

SUBTOPIC: Strategy: Examine Error Messages
<ul>
    <li>sometimes it is very obvious that code has a bug since it crashes and gives an error message
    </li>
    <li>we can examine these error messages to see what we are doing wrong
    </li>
    <li>in python, the error message is called an error message is called a traceback
    </li>
    <li>a traceback tells you what line you made an error in, and how it got there
    </li>
    <li>we can't add integers to strings
    </li>
</ul>

SUBTOPIC: Strategy: Work from a Working Example
<ul>
    <li>programmers try making random changes to their non working code
    </li>
    <li>try debugging step by step
    </li>
</ul>

SUBTOPIC: Strategy: Check Intermediate Results
<ul>
    <li>bugs that crash our code are harder to fix than bugs that don't
    </li>
    <li>we can remove parts of strings:
    </li>
    <ul>
        <li># Try adding print statements to look at the values of variables inside
        </li>
        <li># the remove function.  See if you can find out what's making it give
        </li>
        <li># silly answers such as remove('ding', 'do') -> 'dining'.
        </li>
        <li>   * def remove(somestring, sub):
        </li>
        <li>    "Return somestring with sub removed."
        </li>
        <li>    location = somestring.find(sub)
        </li>
        <li>    length = len(sub)
        </li>
        <li>    part_before = somestring[:location]
        </li>
        <li>    part_after = somestring[location + length:]
        </li>
        <li>    if sub not in somestring:
        </li>
        <li>        return somestring
        </li>
        <li>    return part_before + part_after
        </li>
        <li>   * #
        </li>
        <li># Don't change these test cases!
        </li>
        <li>print remove('audacity', 'a')
        </li>
        <li>print remove('pythonic', 'ic')
        </li>
        <li>print remove('substring institution', 'string in')
        </li>
        <li>print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
        </li>
        <li>print remove('doomy', 'dooming')  # and this should print "doomy"
        </li>
    </ul>
</ul>

SUBTOPIC: Strategy: Keep and Compare Old Versions
<ul>
    <li>if you want to see old versions of code, you can comment out the old versions
    </li>
    <li>you can also copy the separate versions into different files
    </li>
    <li>you can also use github
    </li>
</ul>

SUBTOPIC: Debugging as a Scientific Process
<ul>
    <li>debugging is a scientific process that helps you find stuff in your code that you did not expect there
    </li>
    <li>correctly locating errors is a big part of writing reliable software
    </li>
</ul>

TOPIC: Stage 2: Work Session 4

SUBTOPIC: Practice Part 2
<ul>
    <li>in modular code, the "data" is separated from its visual presentation so that you can change one without worrying about the other
    </li>
</ul>

SUBTOPIC: Step 2: Make a Strategy [slides]
<ul>
    <li>if we want to write code that takes in text and spits out the text in HTML that we can use for our web page, we need to write a function
    </li>
    <li>in this case, it would be a terrible idea to try and get all of the output with just one function since it is too much to do all at once
    </li>
    <li>instead, we should use just one concept at a time
    </li>
    <ul>
        <li>this will require a simpler function
        </li>
        <ul>
            <li>this function will have to accept a second input so we can tell it which concept to make HTML for
            </li>
        </ul>
        <li>now that we have compressed the problem, we can think about how to solve it
        </li>
        <li>we can write four smaller functions
        </li>
        <ul>
            <li>get concept by number
            </li>
            <ul>
                <li>get title
                </li>
                <li>get description
                </li>
            </ul>
            <li>generate concept HTML
            </li>
        </ul>
    </ul>
</ul>

TOPIC: 2.6 Structured Data: Lists and For Loops

SUBTOPIC: [ND] Where to Focus Your Attention
<ul>
    <li>we can use for loops to iterate over structured data
    </li>
</ul>

SUBTOPIC: Introduction
<ul>
    <li>the next thing we will need for our web crawler is structured data
    </li>
    <li>the closest thing we have seen to structured data is the string data type
    </li>
    <li>a string is structured data because we can break it down into separate characters
    </li>
    <ul>
        <li>the string is a sequence of characters and we can operate on subsequences of the string
        </li>
    </ul>
    <li>what we can do with strings is somewhat limited since all we can put inside the string is a character
    </li>
    <li>we will learn about the list data type
    </li>
    <ul>
        <li>lists are more powerful than strings because a list can be a sequence of anything, rather than just characters
        </li>
        <ul>
            <li>lists can contain characters, strings, numbers, or even other lists
            </li>
        </ul>
    </ul>
    <li>to identify a list, we use square brackets instead of quotes
    </li>
    <li>just like strings, we can use square brackets to index a list
    </li>
    <li>we can have blank lists
    </li>
    <li>lists have this layout:
    </li>
    <ul>
        <li>&lt;list&gt; &rarr; [&lt;expression&gt;, &lt;expression&gt;, . . . ]
        </li>
    </ul>
    <li>we can use lists in assignment statements
    </li>
</ul>

SUBTOPIC: Nested Lists
<ul>
    <li>we can make lists with mixed elements
    </li>
    <li>if we have a long list and we can not fit it on one line, we can divide it into multiple lines as long as we divide it each time after a comma
    </li>
    <li>we can use multiple indexes to find a an item inside a list item inside a list item and so on
    </li>
</ul>

SUBTOPIC: Mutation
<ul>
    <li>there are two major differences between strings and lists
    </li>
    <ul>
        <li>one is that a list can hold anything we want while strings can only hold characters
        </li>
        <li>the other is that lists support mutation
        </li>
        <ul>
            <li>this means that we can change the value of a list after we have created it
            </li>
            <li>this is powerful, but it also makes our code a lot harder to read and understand
            </li>
        </ul>
    </ul>
    <li>we can assign a variable to a string and change the variable, but we cannot change a string with no variable assigned to it
    </li>
</ul>

SUBTOPIC: A List of Strings
<ul>
    <li>example of mutation:
    </li>
    <ul>
        <li>p = ["H", "e", "l", "l", "o"]
        </li>
        <li>p[0] = "Y"
        </li>
        <li>aliasing is when we have two ways to refer to the same object
        </li>
    </ul>
</ul>

SUBTOPIC: List Operations
<ul>
    <li>append is a method
    </li>
    <ul>
        <li>we can use this to add elements to the end of a list
        </li>
        <li>this mutates the old list
        </li>
        <li>&lt;list&gt;.append(&lt;element&gt;)
        </li>
        <ul>
            <li>this adds &lt;element&gt; to &lt;list&gt; as 1 list item
            </li>
        </ul>
    </ul>
</ul>

SUBTOPIC: List Addition and Length
<ul>
    <ul>
        <li>now, if we print p, we will get:
        </li>
        <li>["Y", "e", "l", "l", "o"]
        </li>
        <li>if we assign the variable q to p, we can change q and that will change p at the same time
        </li>
    </ul>
</ul>

SUBTOPIC: Aliasing
<ul>
    <li>&lt;list&gt; + &lt;list&gt;
    </li>
    <ul>
        <li>like concatenation for strings
        </li>
    </ul>
    <li>len(&lt;list&gt;)
    </li>
    <ul>
        <li>states the length of a string or list
        </li>
        <li>len starts at 1, not 0
        </li>
    </ul>
</ul>

SUBTOPIC: For Loops
<ul>
    <li>for &lt;name&gt; in &lt;list&gt;:
    </li>
    <ul>
        <li>&lt;block&gt;
        </li>
    </ul>
    <li>a variable defined outside (before) a loop and which is changed for each iteration of the loop is called an accumulator
    </li>
    <ul>
        <li>for instance it can represent a sum, a product, or a count
        </li>
    </ul>
    <li>common layout loops:
    </li>
    <ul>
        <li>function
        </li>
        <ul>
            <li>accumulator variable
            </li>
            <li>loop
            </li>
            <ul>
                <li>loop body
                </li>
            </ul>
            <li>return accumulator
            </li>
        </ul>
    </ul>
</ul>

SUBTOPIC: Index
<ul>
    <li>&lt;list&gt;.index(&lt;value&gt;)
    </li>
    <li>this is returns the index of the value in a list, but if the value does not exist in the list, it returns an error rather than -1
    </li>
    <li>if there are more than one occurrences of the value, it gives you the first one
    </li>
instead, we can use &lt;value&gt; in &lt;list&gt;
    <ul>
        <li>this prints true or false
        </li>
        <li>we can also use "not in" , which is the exact opposite
        </li>
    </ul>
</ul>

TOPIC: 2.7 How to Solve Problems
<ul>
    <li>how to solve problems:
    </li>
    <ol>
        <li>Don't Panic!!
        </li>
        <li>What are the inputs?
        </li>
        <li>What are the Outputs?
        </li>
        <li>Work through some examples by hand
        </li>
        <li>Simple mechanical solution
        </li>
        <li>develop incrementally and test as we go
        </li>
    </ol>
    <li>if we say x % y == some number, this is tells you whether it is true or false that x is a multiple of y
    </li>
</ul>

TOPIC: Stage 2: Work Session 5

SUBTOPIC: Exploring List Properties
<ul>
    <li>if we combine two lists using +, we get a list with all of the items in both of the lists
    </li>
    <li>if we combine two lists using append, we end up adding the second list as one of the elements of the first list
    </li>
</ul>

LESSON: Lesson 3: Program With Objects

TOPIC: 3.2 Use Functions

SUBTOPIC: Making the Program Wait Longer
<ul>
    <li>we can use time.sleep() to make our program wait for a certain number of seconds
    </li>
    <li>we can also use time.ctime() to get the current time and date
    </li>
    <ul>
        <li>for both of these, we have to say import time, or import ctime
        </li>
    </ul>
    <li>we can use control+c to stop our program
    </li>
</ul>

SUBTOPIC: Where Does Webbrowser Come From?
<ul>
    <li>inside the Python Standard Library,  are multiple files, which we use to program (like def and webbrowser and time)
    </li>
    <ul>
        <li>inside each of these files are functions which allow the files to work when we use them
        </li>
        <li>the fact that we don't really know what makes these functions work is called abstraction
        </li>
        <li>abstraction is a major idea in programming since it lets us focus on the program we want to write
        </li>
    </ul>
</ul>
"""

print generate_all(TEST_TEXT)
