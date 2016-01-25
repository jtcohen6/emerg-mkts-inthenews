* [Background](#background)
* [Inquiry](#inquiry)
* [Model](#model)
* [Limitations](#limits)
* [Next Steps](#next-steps)
* [Acknowledgments](#acknowledge)


## Visualization Setup

Open terminal and run the following:
```ruby
python -m SimpleHTTPServer [LocalHost] (e.g., 8000, 5000)

```
This will render the visualization of 4 time series that compares ETFs of the chose country with the sentiment scores. 


<a id="background"></a>
## Background: emerging, encouraging, splurging, purging

We may not be at the biggest nerd convention after all.

As we hack this, leaders and technocrats from around the world are meeting at the [World Economic Forum](http://www.weforum.org/) in Davos, Switzerland. And ["high-altitude networking"](http://nyti.ms/1OsFHUO) though it may be, there are real concerns about the future of globalist paradigms in finance and macroeconomic policy.

High-yield "junk" bonds, especially those from "emerging markets", experienced a sharp "correction" in late 2015. The investor jargon is useful to a point: asset classes, like skirt lengths, go up and down as a matter of fashion.

A slow-down in the once indefatigable Chinese economy, alongside decades-low commodity prices, seems poised to undermine older projections of the economic world to come. Voracious growth among developing ("emerging") countries---rich in natural resources and cheap labor, whether in South and Southeast Asia, the Gulf States, West Africa, or South America---cannot continue on 5+% GDP growth year over year.

Out of skeptical curiosity, though not cynicism, [we might consider possibilities](http://www.newyorker.com/news/john-cassidy/what-is-the-post-post-davos-model-of-the-world):
1. The globalized economic structure is undergoing a long-term stress test (whether "debt supercyle" or "secular stagnation");
2. The globalized _financial_ structure is more liable to the momentum of well-informed investor band-wagoning.

<a id="inquiry"></a>
## Inquiry: How well informed? Well informed _how?_

_"To prove that Wall Street is an early omen of movements still to come in GNP, commentators quote economic studies alleging that market downturns predicted four out of the last five recessions. That is an understatement. Wall Street indexes predicted nine out of the last five recessions! And its mistakes were beauties."_
<div align=right>Prof. Paul Samuelson</div>

Regular readers of fact-dense, short-form financial news have long benefitted from knowing more, earlier. We're interested in the broader implications: How do emerging-market countries and the international media outlets---serving as intermediary to the wealthy, investing West---inform, influence, and incentivize each other? How can financial reporting itself engender financial phenomena?

<a id="model"></a>
## Model: Our proposed analysis

_Emerging Market:_ A term of investment, endearment, or euphemism referring to those countries with high growth potential, often due to natural resource abundance, infrastructural development, and relative deregulation. Ranging from small polities (qua startups) to 1b-person juggernauts, also called "developing nations" on the basis of human development and GDP-per-capita indices.

_ETF:_ Exchange Traded Funds are attractive for our model because:

* Anyone can buy shares: they're low-cost, tax-effective, and therefore widely held assets
* Unlike mutual funds, they're traded openly on exchanges and usually reflect asset value in price
* They invest in a representative basket of assets & bonds, while often also tracking indices

ETFs are widely disseminated, vulnerable to conventional market forces, and representative of their target sample.

_Aladdin API:_ In addition to a clean .json request process for the need-to-know information about any stock, BlackRock's trading platform offers risk management data and all the bells and whistles of at-your-fingertips analytics. The portfolio modeling functionality was especially helpful in formulating our initial question: _"What if an investor in 2011 had followed only the implicit advice of financial news outlets?"_ BlackRock's API offers the data and interface to get a reasonable answer.

_Media outlets:_ There is a significant dearth of historical journalistic data that is available in bulk and without proprietary licensing. This may have been the most significant challenge and limitation to our project---as in the field. Manual downloading of Forbes and Financial Times, one small cache at a time, suffices for proof of concept. Looking forward, we defer to PhD candidates in Statistics and Computer Science who are working toward similar ends.

_Natural Language Processing:_ Right from the start, the project required some delving into the contemporary work in sentiment analysis. Yet, lacking sufficient media evidence to properly train a neural net, while also hoping for a better algorithm than "bag of words"---made even less workable by the dry tone of our matter of interest, business journalism---we were happy to discover [vaderSentiment](https://github.com/cjhutto/vaderSentiment) and [sentlex](https://github.com/bohana/sentlex). Raghav spent many sleepless hours fine-tuning a workable lexicon, and even though we could not run it across all ~25,000 articles, he deserves all the sleep in the world.

<a id="limits"></a>
## Limitations; or, it's just a weekend...

We're not sure how many great regressions you've seen cobbled together in a few days' time---meaning ones with an R^2 above 0.5, let alone those demonstrable insights with earth-shattering implications.

We are proud to have pursued an ambitious goal, one which we also believe to have genuine intellectual merit.

<a id="next-steps"></a>
## Next Steps

Down the line, we hope to be able to work with better-structured data and run more involved natural language processing. The day when conducting larger-scale learning algorithms on public journalism, especially content as consistent as financial reporting, should bring with it new opportunities for research. And, of course, our visualizations could always be more intuitive and prettier.

<a id="acknowledge"></a>
## Acknowledgments

Our sincere thanks to vaderSentiment (Hutto, C.J. & Gilbert, E.E., 2014), sentlex, c3, the BlackRock API, and everyone who made PennApps possible!
