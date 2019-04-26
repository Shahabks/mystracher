![Image](https://github.com/Shahabks/mystracher/blob/master/lo-go.png)

# mystracher
### A structure / Grammar checker of English - Built on AtD, After the Deadline for Python 3.7

## Ver 2 scoring bug fixed

This library is a language checker for English with:

<ul>
  <li> –Contextual Spell Checking</li>
 <li> –Advanced Style Checking</li> 
 <li> –Intelligent Grammar Checking</li>
</ul>

This library was built for Python 3.7. It uses artificial intelligence and natural language processing technology to find your writing errors and offer smart suggestions. The basic technology and vectorization had been developed by After the Deadline (AtD) http://www.afterthedeadline.com/ and is available under the GNU General Public License. 

AtD model is a bit old though enough for the purpose of checking grammar. 

After the Deadline is available on WordPress.com as well as in libraries, plugins, add-ons, and extensions for a variety of platforms. See the Download or Developers page for more information on extensions and libraries.
#### Build on work done by Miguel Ventura, thanks
### Installation 
            pip install mystracher
            
## Use
            import mystracher as dd 
            
            dd.mystracher()
            
    
### output 
[out1]
 
                        =================== RESTART: C:/Users/shahab/Desktop/testtt.py ===================
                        
#### Enter the text here:      
#### Politics (from Greek: πολιτικά, translit. Politiká, meaning "affairs of the cities") refers to a set of activities associated with the governance of a country, or an area. It involves making decisions that apply to members of a group.[1]It refers to achieving and exercising positions of governance—organized control over a human community, particularly a state.[2] The academic study focusing on just politics, which is therefore more targeted than general political science, is sometimes referred to as politology (not to be confused with politicology, a synonym of political science).
#### In modern nation-states, people have formed political parties to represent their ideas. They agree to take the same position on many issues and agree to support the same changes to law and the same leaders.[3] An election is usually a competition between different parties.[4] Some examples of political parties worldwide are: the African National Congress (ANC) in South Africa, the Conservative in the United Kingdom, the Christian Democratic Union (CDU) in Germany and the Indian National Congress in India. Politics is a multifaceted word. It has a set of fairly specific meanings that are descriptive and nonjudgmental (such as "the art or science of government" and "political principles"), but does often colloquially carry a negative connotation.[1][5][6] The word has been used negatively for many years: the British national anthem as published in 1745 calls on God to "Confound their politics",[7] and the phrase "play politics", for example, has been in use since at least 1853, when abolitionist Wendell Phillips declared: "We do not play politics; anti-slavery is no half-jest with us."[8] A variety of methods are deployed in politics, which include promoting one's own political views among people, negotiation with other political subjects, making laws, and exercising force, including warfare against adversaries.[9][10][11][12][13] Politics is exercised on a wide range of social levels, from clans and tribes of traditional societies, through modern local governments, companies and institutions up to sovereign states, to the international level. A political system is a framework which defines acceptable political methods within a given society. The history of political thought can be traced back to early antiquity, with seminal works such as Plato's Republic, Aristotle's Politics and the works of Confucius. Economics (/ɛkəˈnɒmɪks, iːkə-/)[1][2][3] is the social science that studies the production, distribution, and consumption of goods and services.[4] Economics focuses on the behaviour and interactions of economic agents and how economies work. Microeconomics analyzes basic elements in the economy, including individual agents and markets, their interactions, and the outcomes of interactions. Individual agents may include, for example, households, firms, buyers, and sellers. Macroeconomics analyzes the entire economy (meaning aggregated production, consumption, savings, and investment) and issues affecting it, including unemployment of resources (labour, capital, and land), inflation, economic growth, and the public policies that address these issues (monetary, fiscal, and other policies). See glossary of economics. Other broad distinctions within economics include those between positive economics, describing "what is", and normative economics, advocating "what ought to be"; between economic theory and applied economics; between rational and behavioural economics; and between mainstream economics and heterodox economics.[5]Economic analysis can be applied throughout society, in business, finance, health care, and government. Economic analysis is sometimes also applied to such diverse subjects as crime, education,[6] the family, law, politics, religion,[7] social institutions, war,[8] science,[9] and the environment.[10] Mathematics (from Greek μάθημα máthēma, "knowledge, study, learning") includes the study of such topics as quantity,[1] structure,[2] space,[1] and change.[3][4][5] Mathematicians seek and use patterns[6][7] to formulate new conjectures; they resolve the truth or falsity of conjectures by mathematical proof. When mathematical structures are good models of real phenomena, then mathematical reasoning can provide insight or predictions about nature. Through the use of abstraction and logic, mathematics developed from counting, calculation, measurement, and the systematic study of the shapes and motions of physical objects. Practical mathematics has been a human activity from as far back as written records exist. The research required to solve mathematical problems can take years or even centuries of sustained inquiry. Rigorous arguments first appeared in Greek mathematics, most notably in Euclid's Elements. Since the pioneering work of Giuseppe Peano (1858–1932), David Hilbert (1862–1943), and others on axiomatic systems in the late 19th century, it has become customary to view mathematical research as establishing truth by rigorous deduction from appropriately chosen axioms and definitions. Mathematics developed at a relatively slow pace until the Renaissance, when mathematical innovations interacting with new scientific discoveries led to a rapid increase in the rate of mathematical discovery that has continued to the present day.[8] Mathematics is essential in many fields, including natural science, engineering, medicine, finance, and the social sciences. Applied mathematics has led to entirely new mathematical disciplines, such as statistics and game theory. Mathematicians engage in pure mathematics (mathematics for its own sake) without having any application in mind, but practical applications for what began as pure mathematics are often discovered later.[9][10]

string:   πολιτικά
description   Spelling
type    spelling
precontext   None
------------
string:   translit
description   Spelling
type    spelling
precontext   None
------------
suggestion:   transit
===============
suggestion:   transmit
===============
string:   Politiká
description   Spelling
type    spelling
precontext   None
------------
suggestion:   Politian
===============
string:   the governance of
description   Hidden Verbs
type    grammar
precontext   with
------------
string:   governanceorganized
description   Spelling
type    spelling
precontext   of
------------
string:   politology
description   Spelling
type    spelling
precontext   as
------------
suggestion:   politely
===============
suggestion:   philology
===============
string:   politicology
description   Spelling
type    spelling
precontext   with
------------
suggestion:   politically
===============
string:   therefore
description   Complex Expression
type    suggestion
precontext   is
------------
suggestion:   (omit)
===============
string:   referred to as
description   Complex Expression
type    suggestion
precontext   sometimes
------------
suggestion:   called
===============
string:   to be
description   Passive voice
type    grammar
precontext   not
------------
πολιτικά (Spelling)
translit (Spelling)
Politiká (Spelling)
the governance of (Hidden Verbs)
governanceorganized (Spelling)
politology (Spelling)
politicology (Spelling)
therefore (Complex Expression)
referred to as (Complex Expression)
to be (Passive voice)
===============
### Score    : 0.6

[out2]
>>> 
                        =================== RESTART: C:/Users/shahab/Desktop/testtt.py ===================
#### Enter the text here:     
#### helllo i are der and i has go here

string:   helllo
description   Spelling
type    spelling
precontext   None
------------
suggestion:   hello
===============
string:   i
description   Make I uppercase
type    grammar
precontext   helllo
------------
suggestion:   I
===============
string:   i
description   Make I uppercase
type    grammar
precontext   and
------------
suggestion:   I
===============
string:   has go
description   Auxiliary Verb Agreement
type    grammar
precontext   i
------------
suggestion:   has gone
===============
helllo (Spelling)
i (Make I uppercase)
i (Make I uppercase)
has go (Auxiliary Verb Agreement)
===============
### Score    : 0.25
>>> 
                                =================== RESTART: C:/Users/ta/Desktop/testtt.py ===================
#### Enter the text here:    
#### jamp on the bed with five dogs

string:   jamp
description   Spelling
type    spelling
precontext   None
------------
suggestion:   jump
===============
suggestion:   jam
===============
suggestion:   jams
===============
suggestion:   jimp
===============
suggestion:   jamb
===============
jamp (Spelling)
===============
Score    : 1.0
>>> 

