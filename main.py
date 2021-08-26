import discord
import os
import random
client = discord.Client()
from keep_alive import keep_alive
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
# Get a database reference to our blog.
#ref = db.reference('server/tha-savage-boi')
#cred = credentials.Certificate(')

members = []
passwords = []
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Loki Laufeyson
loki_gif = ['https://tenor.com/view/tom-hiddleston-loki-thor-ragnarok-tom-gif-10179470',
 'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-gif-10179468',
 'https://tenor.com/view/tom-hiddleston-loki-thor-tom-hiddleston-gif-10179471', 
 'https://tenor.com/view/tom-hiddleston-loki-thor-ragnarok-tom-gif-10179464', 
 'https://tenor.com/view/tom-hiddleston-loki-tom-hiddleston-gif-10179462', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-7519582', 
 'https://tenor.com/view/tom-hiddleston-laughing-gif-7519592', 
 'https://tenor.com/view/loki-hair-tom-hiddleston-gif-7519604',
 'https://tenor.com/view/tom-hiddleston-quiet-loki-gif-11884544',
 'https://tenor.com/view/tom-hiddleston-loki-gif-10259484', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10259481', 
 'https://tenor.com/view/loki-tom-hiddleston-gif-10342777', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10302664', 
 'https://tenor.com/view/loki-ssh-tom-hiddleston-gif-10342815', 
 'https://tenor.com/view/loki-tom-hiddleston-gif-10342834', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347762',
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347813', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10347822', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-10349035', 
 'https://tenor.com/view/tom-hiddleston-loki-gif-8798528', 
 'https://tenor.com/view/loki-tom-hiddleston-thor-gif-9423972',
 'https://tenor.com/view/rude-loki-mcu-gif-13519119' ]

loki_quotes = ['“I am Loki of Asgard and I am burdened with glorious purpose.” - The Avengers', '“You must be truly desperate to come to me for help.” - Thor: The Dark World', '“There are no men like me.” - The Avengers', '“Enough! You are, all of you are beneath me! I am a god, you dull creature, and I will not be bullied" - The Avengers', "“Is not this simpler? Is this not your natural state? It’s the unspoken truth of humanity that you crave subjugation. The bright lure of freedom diminishes your life’s joy in a mad scramble for power. For identity. You were made to be ruled. In the end, you will always kneel.” - The Avengers", "“I never wanted the throne, I only ever wanted to be your equal.” - Thor", "I didn’t do it for him.” - Thor: The Dark World", "“I guess I’ll have to go it alone. Like I’ve always done.” - Thor: Ragnarok", "“I assure you, brother, the sun will shine on us again.” - Avengers: Infinity War", "“So I am no more than another stolen relic, locked up here until you might have use of me?” - Thor", "“It hurts, doesn’t it? Being lied to. Being told you’re one thing and then learning it’s all a fiction.” - Thor: Ragnarok", "“You will never be a god.” - Avengers: Infinity War", "“I have been falling… for 30 minutes!” - Thor: Ragnarok", "“I thought you said you knew how to fly this thing?” - Thor: The Dark World", "“You know this is wonderful! This a tremendous idea! Let’s steal the biggest, most obvious ship in the universe and escape in that! Flying around the city, smash it into everything in sight and everyone will see it! It’s brilliant, Thor!” - Thor: The Dark World", "“You lied to me! I’m impressed.” - Thor: The Dark World", "“If it’s all the same to you, I’ll have that drink now.” - The Avengers", "Well done, you just decapitated your grandfather!” - Thor: The Dark World", "“I have to get off this planet.” - Thor: Ragnarok", "“Oh, this is much better. Costume’s a bit much… so tight. But the confidence, I can feel the righteousness surging. Hey, you wanna have a rousing discussion about truth, honor, patriotism? God bless America…” - Thor: The Dark World", "“Your savior is here!” - Thor: Ragnarok", "“Oh dear. Is she dead?” - Thor: The Dark World"]

#Thor Odinson
thor_gif = ['https://tenor.com/view/thor-avenger-chris-hemsworth-mjolnir-gif-13624915', 'https://tenor.com/view/smile-thor-gif-8176906', 'https://tenor.com/view/thor-gif-10494447', 'https://tenor.com/view/fat-thor-avengers-funny-chris-hemsworth-gif-14558486', 'https://tenor.com/view/real-thor-thor-fight-gif-7320950', 'https://tenor.com/view/thor-marvel-comics-avengers-gif-8224887', 'https://tenor.com/view/thor-thor-ragnarok-iagree-approved-christ-hemsworth-gif-17954394', 'https://tenor.com/view/thor-fat-thor-rocket-racoon-rocket-raccoon-gif-14664934', 'https://tenor.com/view/thor-avengers-end-game-gif-13724139', 'https://tenor.com/view/thor-infinity-war-laugh-classic-raining-gif-12263998', 'https://tenor.com/view/be-honest-just-being-is-he-though-gif-13443315', 'https://tenor.com/view/real-thor-gif-7320925', 'https://tenor.com/view/thor-hide-shy-bruce-banner-avengers-gif-11758192', 'https://tenor.com/view/thor-ragnarok-chris-hemsworth-gif-11661868', 'https://tenor.com/view/raining-thor-dancing-thor-moves-gif-12263454', 'https://tenor.com/view/thor-drinks-another-one-coffee-good-gif-14287005', 'https://tenor.com/view/thor-dancing-chris-hemsworth-gif-14079581', 'https://tenor.com/view/thor-ragnarok-nod-chris-hemsworth-thor-yup-gif-14591378', 'https://tenor.com/view/endgame-thor-avengers-waiting-fat-thor-gif-13031996', 'https://tenor.com/view/thor-thor-odinson-thor-ragnarok-smile-marvel-gif-17291489', 'https://tenor.com/view/thor-come-on-you-love-it-thor-ragnarok-loki-ihate-it-gif-11512840', 'https://tenor.com/view/thor-hammer-mjolnir-its-all-in-the-swing-avengers2-gif-7373971', 'https://tenor.com/view/thor-ragnarok-transform-gif-14601550', 'https://tenor.com/view/avengers-reaction-thor-gif-9853221', 'https://tenor.com/view/so-cool-thor-chris-hemsworth-avengers-infinity-war-happy-gif-11811009', 'https://tenor.com/view/panic-attack-thor-fat-thor-gif-14801579', 'https://tenor.com/view/thor-chris-hemsworth-hunk-smile-gif-12147789', 'https://tenor.com/view/thor-ragnarok-chris-hemsworth-fail-because-thats-what-gif-14021864', 'https://tenor.com/view/thor-thor-ragnarok-thor-odinson-marvel-mcu-gif-17305730', 'https://tenor.com/view/thor-gif-8734201', 'https://tenor.com/view/thor-avengers-infinity-war-thunder-lightning-gif-15116476', 'https://tenor.com/view/thor-hammer-gif-7320952', 'https://tenor.com/view/head-tilt-huh-thor-gif-14837349', 'https://tenor.com/view/thorki-thor-and-loki-thor-loki-happy-gif-19894207', 'https://tenor.com/view/thor-in-my-brain-now-in-my-head-thor-ragnarok-chris-hemsworth-gif-12390465', 'https://tenor.com/view/thor-down-electricity-gif-19701021']

thor_quotes = ['“This drink, I like it! ANOTHER!” (Thor, 2011)', '“Do I look to be in a gaming mood?” (The Avengers, 2012)', '“You people are so petty, and tiny.” (The Avengers, 2012)', '“You’re big. I’ve fought bigger.” (Thor, 2011)', '“You should know that when you betray me, I will kill you.” (Thor: The Dark World, 2013)', '“He’s adopted.” (The Avengers, 2012)', '“Fortunately, I am mighty!” (The Avengers: Age of Ultron, 2015)','"Is He, Though?"', '"I Went For The Head."', '"Im Still Worthy."', '“THIS DRINK, I LIKE IT! ANOTHER!”', '“I CHOOSE TO RUN TOWARD MY PROBLEMS AND NOT AWAY FROM THEM...”', '“THANK YOU, SWEET RABBIT.”', '"Because thats what heroes do"', '“I’M ONLY ALIVE BECAUSE FATE WANTS ME ALIVE.”', '“HE’S A FRIEND FROM WORK!”', '“YEAH, IT’S CALLED THE…REVENGERS!”', '“THERE WAS ONE TIME MY BROTHER TRANSFORMED HIMSELF INTO A SNAKE...”', '“I NOTICE YOUVE COPIED MY BEARD.”']

#Tony Stark
tony_gif = ['https://giphy.com/gifs/iron-man-tony-stark-ovaries-5bGYUuT3VEVLa',
'https://giphy.com/gifs/kiss-fRtaYXfsfBlcY', 
'https://giphy.com/gifs/iron-man-tony-stark-pepper-potts-12nyqXsnSLt6k8',
'https://giphy.com/gifs/yes-nod-robert-downey-jr-kulp9iNdguU1O',
'https://giphy.com/gifs/iron-man-eye-roll-disgust-qmfpjpAT2fJRK',
'https://giphy.com/gifs/marvel-tony-stark-PW7LUFutrNwJi',
'https://giphy.com/gifs/robert-downey-jr-the-avengers-tony-stark-uZjLDqG3PTGA8',
'https://giphy.com/gifs/robert-downey-jr-the-avengers-tony-stark-hhkxS5FlLSwtq',
'https://giphy.com/gifs/captain-america-civil-war-cacw-hjeLCjLA3YDXa',
'https://giphy.com/gifs/robert-downey-jr-tony-stark-1000-8ltyoIL6d7uZG',
'https://giphy.com/gifs/robert-downey-jr-avengers-iron-man-P2a7oxnUULoys',
'https://giphy.com/gifs/funny-robert-downey-jr-iron-man-rlsHtd2YC8k0g',
'https://giphy.com/gifs/happy-smiling-robert-downey-jr-wWuYQaUeCVJmw',
'https://giphy.com/gifs/robert-downey-jr-iron-man-tony-stark-rOGfF40uFHwxa',
'https://giphy.com/gifs/iron-man-2-jon-favreau-1MwnwxYu69cNq',
'https://giphy.com/gifs/disappointed-bummed-2d400VBPJbxaU',
'https://giphy.com/gifs/reaction-tony-stark-50fuVHMGUVszu',
'https://giphy.com/gifs/tony-stark-iron-man-3-pepper-potts-2WLQYjYONpqBq',
'https://giphy.com/gifs/iron-man-tony-stark-maestro-hHxTQkcjmHUTC',
'https://giphy.com/gifs/robert-downey-jr-the-avengers-clark-gregg-bRDqRstCzPln2',
'https://giphy.com/gifs/reaction-avengers-tony-stark-12rbefTh33TNTi',
'https://giphy.com/gifs/robert-downey-jr-iron-man-the-avengers-AoTzzu7XUJCwM','https://tenor.com/view/maybe-robert-downey-jr-sherlock-holmes-rdj-gif-4384335']

tony_quotes = ['“The Truth is…I am Iron Man.”',
'“Is it better to be feared or respected? I say, is it too much to ask for both?”',
'“I shouldn’t be alive unless it was for a reason.”', '“Sometimes you gotta run before you can walk.”', '“Iron man. That’s kind of catchy. I mean it’s not technically accurate.”', '“What is the point of owning a race car if you can’t drive it?”', '“Following’s not really my style.”', '“Genius, Billionaire, Playboy, Philanthropist.”', '“if we can’t protect the Earth, you can be damn well sure we’ll avenge it.“', '“We create our own Demons”.', '“I build neat stuff, got a great girl, occasionally save the world. So why can’t I sleep?”', '“One thing you can’t take away? I am Iron Man”', '“If we can’t accept limitations we’re no better than the bad guys.”', '“If you are nothing without the suit, then you shouldn’t have it.”', '“No amount of Money ever bought a second of Time.”', '“Everybody wants a happy ending, right? But it doesnt always roll that way.”', '“Part of the Journey is the End.”', '“What am I even tripping for? Everything is going to work out exactly the way it’s supposed to.”',' “I Love You 3000.”', '“And…I…Am…Iron Man.”', '"I Came To Realize That I Had More To Offer This World Than Just Making Things That Blow Up."', '"Its Not About How Much Weve Lost, Its About How Much We Have Left."', '"Contrary To Popular Belief, I Know Exactly What Im Doing."', '"You Know, It’s Times Like These When I Realize What A Superhero I Am."', '"Textbook Narcissism? Agreed."']

#Steve Rogers
rogers_gif = ['https://tenor.com/view/captain-america-chris-evans-thankyou-salute-gif-4762823', 'https://tenor.com/view/captain-america-avengers-endgame-gif-14090135', 'https://tenor.com/view/captain-america-ican-do-this-all-day-never-quit-gif-12494317', 'https://tenor.com/view/captain-america-avengers-endgame-old-man-idont-think-iwill-gif-14669627', 'https://tenor.com/view/captain-america-gif-9237573', 'https://tenor.com/view/captain-america-winter-soldier-shield-ready-leaving-gif-7373972', 'https://tenor.com/view/captain-america-avengers-dance-moves-happy-gif-16643267', 
'https://tenor.com/view/captain-america-walking-gif-14735617', 'https://tenor.com/view/that-is-america-ass-captain-america-avengers-endgame-gif-14805594', 
'https://tenor.com/view/marvel-captain-america-avengers-chris-evans-reference-gif-5081643', 
'https://tenor.com/view/chris-evans-captain-america-funny-gif-13345825', 
'https://tenor.com/view/chris-evans-captain-america-the-avengers-gif-9034217', 'https://tenor.com/view/captain-america-avengers-avengers-endgame-whatever-it-takes-gif-14766286', 'https://tenor.com/view/captainamerica-steverogers-marvel-heart-encouragement-gif-8415102', 'https://tenor.com/view/captain-america-captain-rogers-steve-rogers-chris-evans-marvel-gif-17938483', 'https://tenor.com/view/infinity-war-steve-rogers-captain-america-chris-evans-gif-11810997', 'https://tenor.com/view/captain-america-avengers-first-avenger-chris-evans-steve-rogers-gif-7371894', 'https://tenor.com/view/captain-america-on-your-left-gif-14036499', 'https://tenor.com/view/captain-america-are-you-nuts-chris-evans-steve-rogers-marvel-comics-gif-14924408', 'https://tenor.com/view/son-just-dont-captain-america-chris-evans-marvel-gif-15921374']

rogers_quotes = [' "I can do this all day."', '"I dont want to kill anyone, but I dont like bullies; I dont care where theyre from."', '"I got beat up in that alley. And that parking lot. And behind that diner."', '"You start running, theyll never let you stop. You stand up, push back... Cant say no forever right?"', ' "You know, the last time I was in Germany and saw a man standing above everybody else, we ended up disagreeing."', '"For as long as I can remember, I just wanted to do what was right. I guess Im not quite sure what that is anymore. And I thought I could throw myself back in: follow orders, serve. Its just not the same."', '"Before we get started, does anyone want to get out?"', '“The price of freedom is high, it always has been. And its a price Im willing to pay. And if Im the only one, then so be it. But Im willing to bet Im not.”', '“Ultron thinks were monsters. That were whats wrong with the world. This isnt just about beating him. Its about whether hes right.”', '“You get hurt, hurt them back. You get killed... walk it off."', '"This job, we try to save as many people as we can. Sometimes that doesn’t mean everybody. But if we can’t find a way to live with that, then next time maybe nobody gets saved."', ' "Im not looking for forgiveness. And Im way past asking for permission. Earth just lost her best defender. So were here to fight. If you wanna stay in our way... we will fight you, too."', ' "We don’t trade lives, Vision.”', '"I know it is. Cause I dont know what Im gonna do if it doesnt."']

#Korg
korg_gif = ['https://tenor.com/view/the-revolution-has-begun-area51-ready-to-attack-gif-15323378', 'https://tenor.com/view/piss-of-ghost-thor-ragnarok-korg-gif-11423629',
'https://tenor.com/view/korg-thor-ragnorak-gif-11236441', 'https://tenor.com/view/over-here-waving-korg-thor-ragnarok-gif-14586261', 'https://tenor.com/view/korg-another-day-another-doug-thor-ragnarok-gif-13226519', 'https://tenor.com/view/korg-hey-man-thor-ragnarok-marvel-gif-12237916', 'https://tenor.com/view/korg-thor-gif-10225303', 'https://tenor.com/view/korg-thor-gif-10225293', 'https://tenor.com/view/korg-alien-thor-ragnarok-marvel-the-revolution-has-begun-gif-15091412', 'https://tenor.com/view/korg-thor-gif-10225298', 'https://tenor.com/view/korg-thor-gif-10225297', 'https://tenor.com/view/korg-thorragnarok-ohmygod-gif-19396274', 'https://tenor.com/view/korg-miek-youre-alive-thor-ragnorok-gif-11782923']

korg_quotes = ['"Hey, hey, hey. Hey. Take it easy, man. Over here. The pile of rocks waving at you. Here. Yeah, I am actually a thing. Im a being. Allow me to introduce myself. My name is Korg. I am kind of like the leader in here. I am made of rocks, as you can see. But dont let that intimidate you. You dont need to be afraid unless you are made of scissors. Just a little rock-paper-scissor joke for you."', '"Piss off, ghost!"', '"Another day, another Doug."', '"I tried to start a revolution... but I didnt print enough pamphlets so hardly anyone turned up. Except for my mum and her boyfriend, who I hate. As punishment, I was forced to be in here and become a gladiator. Bit of a promotional disaster that one, but I m actually organizing another revolution. I dont know if you would be interested in something like that? Do you reckon you would be interested?"', '"Oh, yeah, no, this whole thing is a circle...but not a real circle, more like a freaky circle."', '"No, nothing makes sense here, man. The only thing that does make sense is that nothing makes sense."', '"Thats exactly what Doug used to say! See you later, New Doug!"', '"Perishable rocks. There you go. Another one gone."', "Yuck! There’s still someone’s hair and blood all over this. Guys, can you clean up the weapons once you finish your fight? Disgusting slobs", '"Yeah, not really useful unless you’re fighting off three vampires that were huddled together."', '"You rode a hammer?""The hammer rode you on your back?""Oh, my God. The hammer pulled you off?"', '"Sounds like you had a pretty special and intimate relationship with this hammer and that losing it was almost comparable to losing a loved one."', '"Is that some sort of protoplasm, all the stuff that’s coming out of you? Or are they eggs? Looks like eggs."', '"Who’s asking? I know you’re asking. Is anyone else asking, or is it just you?"', '"The revolution has begun!"', '"Oh, Miek is dead. I accidentally stomped on him on the bridge and Ive felt so guilty, Ive been carrying him around all day. Oh, Miek, you are alive! He is alive, guys. What was the question again, bruv?"', '"Hey, man. Im Korg. We are gonna get outta here on that big spaceship. Wanna come?"', '"Thor, he is back. That kid on the TV just called me a dickhead again."']

#Hulk
hulk_gif = ['https://tenor.com/view/hulk-avengers-puny-god-hulk-smash-gif-14162197', 
'https://tenor.com/view/hulk-roar-avengers-infinity-war-angry-gif-11873427', 'https://tenor.com/view/hulk-smash-gif-12896779', 'https://tenor.com/view/hulk-punch-thor-gif-11597097', 'https://tenor.com/view/thumbs-up-hulk-the-hulk-bruce-banner-mark-ruffalo-gif-14705593', 'https://tenor.com/view/the-avengers-the-hulk-im-always-angry-angry-irritated-gif-4166610', 'https://tenor.com/view/hulk-smash-loki-avengers-puny-gif-12082780', 'https://tenor.com/view/hulk-ihate-everything-gif-3438562', 'https://tenor.com/view/hulk-nod-here-you-go-taco-gif-14805610','https://tenor.com/view/professor-hulk-hulk-bruce-banner-marvel-avengers-gif-14109671', 'https://tenor.com/view/hulk-professor-hulk-smart-marvel-sure-gif-14703276', 'https://tenor.com/view/hulk-professor-hulk-bruce-banner-avengers-endgame-gif-14109719', 'https://tenor.com/view/hulk-endgame-time-travel-hulk-timetravel-professor-hulk-gif-14123714']

hulk_quotes = ['" I am always angry."', '"Puny God"', '"There is an Ant-Man AND a Spider-Man?"', '"I don’t want to fight your sister. That’s a family issue."', '"Oh, no, we are way past that. I could choke the life out of you and never change a shade."', '"But Hulk like real fire. Like... raging fire. Thor like smoldering fire."', '"So you are saying that the Hulk, the other guy, saved my life? That is nice. Its a nice sentiment. Save it for what?"', '"What? I see this as an absolute win"', '"You dont. But the radiation is mostly gamma. Its like I was made for this"', '"I dont know how to fly this thing! My PHDs are not to fly alien spaceships"', '" Eighteen months in the gamma lab, I put the brains and the brawn together and now look at me. Best of both worlds."', '"I’ve got a compelling reason not to lose my cool"', '"You know, sometimes exactly what I want to hear isnt exactly what I want to hear."', '"I dont think we should be focusing on Loki. That guy''s brain is a bag full of cats. You can smell crazy on him."', '"Broke up? Like a band? Like the Beatles?"', '"I feel like I know you, too."', '"I don’t know why everyone believes that, but that isn’t true. Think about it: If you travel to the past, that past becomes your future, and your former present becomes the past! Which can’t now be changed by your new future!”"']

#Nat
nat_gif = ['https://giphy.com/gifs/scarlett-johansson-black-widow-natasha-romanoff-fcGuamXXetf5S', 'https://giphy.com/gifs/robert-downey-jr-marvel-black-widow-VKFfxB2skRYZO', 'https://giphy.com/gifs/black-widow-the-avengers-scarlet-johansson-4AD7J5t1j8sco', 'https://giphy.com/gifs/film-news-vZwQtD53HvrmE', 'https://giphy.com/gifs/avengers-marveledit-the-age-of-ultron-KCKYpQ3yOtgJy', 'https://giphy.com/gifs/the-avengers-flQwGOUFYuI2A', 'https://giphy.com/gifs/scarlett-johansson-film-NtuL7EUjEjuoM', 'https://giphy.com/gifs/women-scarlet-johansson-picking-up-after-you-boys-dZ9M5uGszqZyzOt5kU', 'https://giphy.com/gifs/marvel-mcu-cinematic-universe-PkGO3P32fkTsRDZFZ0', 'https://giphy.com/gifs/nerdist-marvel-mcu-black-widow-SssBmdVj1L0MgrFxwE', 'https://giphy.com/gifs/marveledit-natasha-romanoff-avengersedit-5QE1WMD7g5hNC', 'https://giphy.com/gifs/marveledit-natasha-romanoff-avengersedit-Zzak2Yc1rm608', 'https://giphy.com/gifs/hunterress-johansson-romanoff-lRVKw8Pyl8mgU', ]

nat_quotes = ['"Im multitasking."', '"Let me put you on hold."', '"The person who developed this is slightly smarter than me. Slightly."', '"Im sorry. Did I step on your moment?"', '"I blew all my covers. I gotta go figure out a new one."', '"I only ACT like I know everything."', '"He is also a huge dork. Chicks dig that!"', '"Im Always Picking Up After You Boys..."', '"Even If There is A Small Chance We Can Undo This, I Mean, We Owe It To Everyone Not In This Room To Try."', '"This Is Just Like Budapest All Over Again."', '“Either One Of You Know Where The Smithsonian Is? I’m Here To Pick Up A Fossil.”', '“Steve, You Know What’s About To Happen. Do You Really Want To Punch Your Way Out Of This?”', '“You Want To Help? Keep The Car Running.”', '“We Have What We Have When We Have It.”', '“I Get Emails From A Raccoon. Nothing Sounds Crazy Anymore.”', '“She’s Not Alone.”', '“At Some Point, We All Have To Choose Between What The World Wants You To Be And Who You Are.”']

#Bucky
buck_gif = ['https://giphy.com/gifs/lSJftQnSqHXorByEYi', 'https://giphy.com/gifs/mcu-falcon-winter-soldier-EZOZ3VbWpYPoLOGtcR', 'https://tenor.com/view/bucky-sebastian-stan-bucky-barnes-marvel-stare-gif-5654322', 'https://tenor.com/view/sebstan-bucky-gif-9514055', 'https://tenor.com/view/sebastian-stan-bucky-barnes-civil-war-gif-5445582', 'https://tenor.com/view/smiling-laughing-bucky-gif-14735690', 'https://tenor.com/view/seb-cheer-gif-9832781', 'https://tenor.com/view/bucky-bucky-barnes-winter-soldier-the-falcon-and-the-winter-soldier-gun-gif-16216514', 'https://tenor.com/view/sebastian-stan-winter-soldier-happy-gif-5450055', 'https://tenor.com/view/bucky-barnes-captain-america-first-avenger-sebastian-stan-gif-14676504', 'https://tenor.com/view/sebastian-stan-bucky-barnes-im-just-saying-idont-know-what-im-doing-gif-14778399', 'https://tenor.com/view/sebastian-stan-bucky-bucky-barnes-gif-5443074', 'https://tenor.com/view/hide-marvel-thor-bucky-mcu-gif-17045542', 'https://tenor.com/view/bucky-shrug-gif-9767380', 'https://tenor.com/view/sebastian-stan-superman-diss-superman-vs-bucky-bucky-gif-5485916','https://tenor.com/view/bucky-barnes-winter-soldier-motorcycle-sebastianstan-the-falconand-the-winter-soldier-gif-19609600', 'https://tenor.com/view/sestan-bucky-gif-9514065', 'https://tenor.com/view/captain-america-captain-america-vs-bucky-cap-vs-bucky-cap-bucky-gif-14107653', 'https://tenor.com/view/bucky-seb-stan-smile-gif-9767437']

buck_quotes = ['"Could You Move Your Seat?"', '"It Always Ends In A Fight."', '"I Thought You Were Smaller."', '"Who The Hell Is Bucky?"', '"Im With You Til The End Of The Line, Pal."', '"You are My Mission."', '"That Little Guy From Brooklyn Who Was Too Dumb To Run Away From A Fight, I am Following Him."', '"Hey. Pick on someone your own size."', '"The 107th. Sergeant James Barnes, shipping out for England first thing tomorrow."', "You don't have one of those, do you?"]

clint_gif = ['https://tenor.com/view/hawkeye-clint-barton-avengers-gif-10724659', 'https://tenor.com/view/clint-barton-got-him-hawk-eye-gif-10732907', 'https://tenor.com/view/endgame-avengers-hawkeye-clint-barton-dont-give-me-hope-gif-15254733', 'https://tenor.com/view/avengers-endgame-hawkeye-no-please-no-no-sad-gif-16886381', 'https://tenor.com/view/hawkeye-avengers-gif-19884091', 'https://tenor.com/view/jeremy-renner-shrug-hawk-eye-avengers-clint-barton-gif-11778823', 'https://tenor.com/view/itcantbeundone-hawkeye-gif-18781969', 'https://tenor.com/view/hawkeye-thanks-iwill-get-out-of-here-gif-18733863'] 

clint_quotes = ['"You And I Remember Budapest Very Differently."', '"You Want Me To Slow Him Down, Sir? Or Are You Sending In More Guys For Him To Beat Up?"', '"Nobody Would Know. Nobody. Yeah. The Last I Saw Him, Ultron Was Sitting On Him."', '"I have Done The Whole Mind Control Thing. Not A Fan."', '"If I Put An Arrow Through Loki s Eye Socket I would Sleep Better, I Suppose."', '"...But If You Step Out That Door, You Are An Avenger."', '"We have Come A Long Way Since Budapest."', '"I Wish There Was A Way That I Could Let Her Know."', '"You Survived. Half The Planet Didn not. They Got Thanos. You Get Me."', '"The City Is Flying, We’re Fighting An Army Of Robots, And I Have A Bow And Arrow. None Of This Makes Sense."']

#Spider Man
spidey_gif = ['https://tenor.com/view/tomholland-peterparker-spiderman-thumbs-up-gif-9294357', 'https://tenor.com/view/hey-everyone-spider-man-gif-7996598', 'https://tenor.com/view/spider-man-crying-shower-sad-bathroom-gif-17172080', 'https://tenor.com/view/spiderman-relaxed-relaxing-chilling-gif-12689909', 'https://tenor.com/view/thumbs-up-two-thumbs-up-spiderman-spiderman-far-from-home-marvel-gif-16527996', 'https://tenor.com/view/spiderman-far-from-home-what-the-no-oh-no-gif-14496402', 'https://tenor.com/view/miles-morales-spider-man-thinking-peter-parker-gif-17729320', 'https://tenor.com/view/spider-sense-thinking-headache-spiderman-spiderverse-gif-12678047', 'https://tenor.com/view/spider-man-tom-holland-bored-gif-11346277', 'https://tenor.com/view/spider-man-flying-superhero-sky-gif-14534295', 'https://tenor.com/view/what-curious-confused-doubtful-look-back-gif-13295202', 'https://tenor.com/view/spiderman-tom-holland-infinity-war-avengers-gif-11811176', 'https://tenor.com/view/spider-man-yoink-marvel-mcu-spider-man-homecoming-gif-19232537', 'https://tenor.com/view/thumbs-up-spider-man-gif-14054574', 'https://tenor.com/view/see-ya-yes-spiderman-into-the-spider-verse-gif-13972481', 'https://tenor.com/view/spider-man-miles-morales-ps5-spider-man-miles-morales-video-games-gif-18804874', 'https://tenor.com/view/spider-man-gif-19682798', 'https://tenor.com/view/spider-man-tom-holland-gif-11346275', 'https://tenor.com/view/spider-man-tom-holland-gif-11346282', 'https://tenor.com/view/spider-man-tom-holland-gif-11346280', 'https://tenor.com/view/spider-man-tom-holland-five-is-good-gif-15223081', 'https://tenor.com/view/spider-man-tom-holland-laugh-cute-handsome-gif-15161593', 'https://tenor.com/view/tom-holland-spider-man-gif-18766751', 'https://tenor.com/view/spider-man-tom-holland-look-out-gif-11346279', 'https://tenor.com/view/peter-parker-spider-man-tom-holland-gif-10917465', 'https://tenor.com/view/spider-man-spider-man-far-from-home-tom-holland-sunglasses-edith-gif-17748816', 'https://tenor.com/view/spider-man-tom-holland-time-out-hand-gesture-gif-15160475', 'https://tenor.com/view/happy-tom-holland-spider-man-gif-14779663']

spidey_quotes = ['“I just wanted to be like you.”', '“I can’t go to Germany. I got homework.” ', '“I’m sick of Mr. Stark treating me like a kid.”', 'I just want to go on a trip with my friends.”', '“I’m sorry I can’t remember anybody’s names!”', '“I just really miss him. Everywhere I go, I see his face.”', '“Cap–Captain. Big fan, I’m Spider-Man.”', '“She was really nice and bought me a churro.”  ', '“Let me just say, if aliens wind up implanting eggs in my chest or something and I eat one of you, I’m sorry.”', '“You can’t be a friendly neighborhood Spider-Man if there’s no neighborhood…Okay, that didn’t really make sense. But you get what I’m trying to say.”']

#Ant mam
antman_gif = ['https://tenor.com/view/dancing-dance-ant-man-paul-rudd-gif-13579286', 'https://tenor.com/view/antman-paul-rudd-coffee-morning-hmm-gif-8951709', 'https://tenor.com/view/paul-rudd-ant-man-iknow-it-wasnt-my-idea-gif-10458098', 'https://tenor.com/view/marvel-marvel-cinematic-universe-ant-man-paul-rudd-gif-14012986', 'https://tenor.com/view/paul-rudd-antman-celebrating-feeling-good-sassy-gif-4967230', 'https://tenor.com/view/antman-scott-lang-paul-rudd-shrug-getting-away-gif-11811006', 'https://tenor.com/view/ant-man-scott-lang-paul-rudd-marvel-ant-gif-10724702', 'https://tenor.com/view/marvel-confused-what-paul-rudd-evangeline-lilly-gif-12127899', 'https://tenor.com/view/civil-war-antman-fight-captain-america-marvel-gif-5949264', 'https://tenor.com/view/antman-tea-going-to-make-some-tea-paul-rudd-gif-4896477', 'https://tenor.com/view/civil-war-antman-fight-captain-america-marvel-gif-5949264', 'https://tenor.com/view/avengers-endgame-antman-paul-rudd-gif-13063176', 'https://tenor.com/view/ant-man-and-the-wasp-shrink-shrinking-tall-girl-tall-gif-17881024', 'https://tenor.com/view/tony-stark-ant-man-avengers-gif-14679826', 'https://tenor.com/view/ant-man-marvel-hi-hello-wave-gif-17105164', 'https://tenor.com/view/ant-man-baskin-robins-dude-you-stupid-gif-14167021', 'https://tenor.com/view/avengers-endgame-paul-rudd-scott-lang-ant-man-scott-lang-ant-man-gif-18084888', 'https://tenor.com/view/ant-man-the-wasp-hank-pym-hi-champ-how-was-school-gif-14051174', 'https://tenor.com/view/that-was-alot-scarier-asecond-ago-ant-man-scottlang-gif-10724700']

antman_quotes = ['Okay, The First Thing We Should Do...Is Call The Avengers.”', '“Anyone See A Southern Gentleman Carrying A Building?”', '“As Far As I’m Concerned, That’s America’s Ass.”', '“Hats And Sunglasses? That’s Not A Disguise, Hank. We Look Like Ourselves At A Baseball Game.”', '“Everything Is Unpredictable. Is That Anybody’s Sandwich? I’m Starving.”', '“I’m Gonna Call Him Antony.”', '“So, Back To The Future’s A Bunch Of Bulls**T?”', '“No, No Whistling! This Isn’t The Andy Griffith Show.”', '“Hold On, You Gave Her Wings?!”', '“I Know You Know A Lot Of Super-People, So...Thinks For Thanking Of Me!”']

#Rhodey
rhodes_gif = ['https://tenor.com/view/marvel-war-machine-civil-rhodes-gif-5357549', 'https://tenor.com/view/rhodey-doncheadle-war-machine-avengers-endgame-gif-14731127', 'https://tenor.com/view/war-machine-james-rhodes-rhodey-mech-suit-air-force-gif-17816394', 'https://tenor.com/view/captain-marvel-rhodey-brie-larson-don-cheadle-the-avengers-gif-17342522', ]

rhodes_quotes = ['“This Lone Gunslinger Act Is Unnecessary. You Don’t Have To Do This Alone!”', '“Cheez Whiz?”', '“OK, Tiny Dude Is Big Now. He’s Big Now.”', '“When You Break Into A Place Called ‘The Temple Of The Power Stone,’ There’s Usually A Bunch Of Booby Traps.”', '“Now, This Is Going To Be A Good Story!”', '“WAR MACHINE ROX,’ With An ‘X.’ All Caps.”', '“So...He’s An Idiot?”', '“Table For One, Mr. Stank. Please, By The Bathroom.”', '“That’s Cute. Thanos Has A Retirement Plan.”', '“If You Want This Suit, You’re Going To Have To Pry My Cold Dead Body Out Of It.”', ]



capmarvel_gif = ['https://tenor.com/view/captain-marvel-carol-danvers-gif-13152837', 'https://tenor.com/view/brie-hangloose-gif-13619777', 'https://tenor.com/view/carol-danvers-captain-marvel-angry-gif-18395009', 'https://tenor.com/view/carol-danvers-captain-marvel-adoragoddess-gif-19226747', 'https://tenor.com/view/laughing-captain-marvel-gif-13355501', 'https://tenor.com/view/avengers-endgame-captain-marvel-you-got-something-for-me-brie-larson-avengers-gif-16835845', 'https://tenor.com/view/captain-marvel-brie-larson-walk-serious-gif-12538895', 'https://tenor.com/view/brie-larson-carol-danvers-capit%c3%a3marvel-captain-marvel-gif-14123204', 'https://tenor.com/view/captain-marvel-oh-yeah-nodding-brie-larson-gif-14587388', 'https://tenor.com/view/captain-marvel-brie-larson-funny-blarg-capitana-gif-13733569', 'https://tenor.com/view/captain-marvel-brie-larson-gif-19527553', 'https://tenor.com/view/king-kong-tom-hiddleston-brie-larson-gif-5718442']

capmarvel_quotes = ['“This Is not About Fighting Wars. Its About Ending Them.”', '“Tell The Supreme Intelligence That I’m Coming To End It. The War, The Lies, All Of It.”', '“If There Are Lives At Stake, I will Fly The Plane.”', '“Call Me Young Lady Again, And I’m Gonna Put My Foot In A Place It is Not Supposed To Be.”', '"Grunge Is A Good Look For You.”', '“I’m Not Gonna Fight Your War, I’m Going To End It.”', '“Higher Further Faster, Baby.”', '“ I’ve Been Fighting With One Arm Behind My Back. What Happens When I am Finally Set Free?”', '"I was already slipping when you happened to punch me in the face. The two events are not related."', ]

wong_gif = ['https://tenor.com/view/dr-strange-doctor-strange-wong-avengers-marvel-gif-15641904', 'https://giphy.com/gifs/avengers-infinity-war-wong-vN1NReVO5CT7Z3GvB2', ]

wong_quotes = ['"What? You wanted more?"', "Attachement from the material is detachment from the spiritual", '"Choose your weapon wisely. No one steps foot in this Sanctum. No one."', '"This section is for masters only, but at my discretion, others may use it. You should start with Maxim s Primer. How’s your Sanskrit?"', ]

happy_gif = []
happy_quotes = []

rocket_gif = []
rocket_quotes = []

starlord_gif = []
starlord_quotes = []

pepper_gif = []
pepper_quotes = []

thanos_gif = []
thanos_quotes = []

strange_gif = []
strange_quotes = []

blackpanther_gif = []
blackpanther_quotes = []


gamora_gif = []
gamora_quotes = []

wanda_gif = []
wanda_quotes = []

vision_gif = []
vision_quotes = []

falcon_gif = []
falcon_quotes = []



mantis_gif = []
mantis_quotes = []

drax_gif = []
drax_quotes = []

shuri_gif = []
shuri_quotes = []

mariahill_gif = []
mariahill_quotes = []

ned_gif = []
ned_quotes = []

groot_gif = []
groot_quotes = []

fury_gif = []
fury_quotes = []

mbaku_gif = []
mbaku_quotes = []

ebonymaw_gif = []
ebonymaw_quotes = []

val_gif = []
val_quotes = []

ancientone_gif = []
ancientone_quotes = []

peggy_gif = []
peggy_quotes = []


hankpym_gif = []
hankpym_quotes = []

stanlee_gif = []
stanlee_quotes = []




@client.event
async def on_message(message):
    if message.author == client.users:
      return

    if message.content.startswith('*help'):
        embedVar = discord.Embed(
            title="Hello there.",
            description=
            '''Welcome to Marvel Bot!! Commands for this bot are as follows:


      ** *tonygif/quotes**      : get Tony Stark gifs/quotes.
      
      ** *lokigif/quotes **     : get Loki gif/quotes
       
      ** *thorgif/quotes **      : get Thor gif/quotes
   
      ** *rogersgif/quotes **    : get Captain's gif/quotes
      
      ** *korggif/quotes **     : get Korg gif/quotes
      
      ** *hulkgif/quotes **     : get Hulk gif/quotes

      ** *natgif/quotes **      : get Black Widow

      ** *buckygif/quotes **    : get Bucky gif/quotes

      ** *clintgif/quotes **    : get Hawkeye's gif/quotes

      ** *spideygif/quotes **    : get Spidey's gif/quotes

      ** *antmangif/quotes **    : get AntMan's gif/quotes
      
      ** *rhodesgif/quotes **    : get Rhodey's gif/quotes

      ** *capmarvelgif/quotes ** : get Captain Marvel's gif/quotes
      
      ** *wonggif/quotes **      : get Wong's gif/quotes
    
      
      ''',
            color=0x00ff00)

        await message.channel.send(embed=embedVar)
    #bcos help will be given to those who ask for it
    #huff i am so bas at writing comments
    #i write comments more than the code itself 

    #moving on


    #Loki Laufeyson
    if message.content.startswith('*lokigif'):
      await message.channel.send(random.choice(loki_gif))
    
    if message.content.startswith('*lokiquotes'):
      await message.channel.send(random.choice(loki_quotes))


    #Thor
    if message.content.startswith('*thorgif'):
       await message.channel.send(random.choice(thor_gif))
    
    if message.content.startswith('*thorquotes'):
      await message.channel.send(random.choice(thor_quotes))

    
    #Tony Stark
    if message.content.startswith('*tonygif'):
      await message.channel.send(random.choice(tony_gif))
    
    if message.content.startswith('*tonyquotes'):
      await message.channel.send(random.choice(tony_quotes))
    
   
    #Steven Rogers
    if message.content.startswith('*rogersgif'):
      await message.channel.send(random.choice(rogers_gif))
    
    if message.content.startswith('*rogersquotes'):
      await message.channel.send(random.choice(rogers_quotes))


    #Korg
    if message.content.startswith('*korggif'):
      await message.channel.send(random.choice(korg_gif))
    
    if message.content.startswith('*korgquotes'):
      await message.channel.send(random.choice(korg_quotes))

    
    #Hulk
    if message.content.startswith('*hulkgif'):
      await message.channel.send(random.choice(hulk_gif))
    
    if message.content.startswith('*hulkquotes'):
      await message.channel.send(random.choice(hulk_quotes))

    
    #Nat
    if message.content.startswith('*natgif'):
      await message.channel.send(random.choice(nat_gif))
    
    if message.content.startswith('*natquotes'):
      await message.channel.send(random.choice(nat_quotes))

    #Buck
    if message.content.startswith('*buckygif'):
      await message.channel.send(random.choice(buck_gif))
    
    if message.content.startswith('*buckyquotes'):
      await message.channel.send(random.choice(buck_quotes))


     
     #clint
    if message.content.startswith('*clintgif'):
      await message.channel.send(random.choice(clint_gif))
    
    if message.content.startswith('*clintquotes'):
      await message.channel.send(random.choice(clint_quotes))

    #Spidey
    if message.content.startswith('*spideygif'):
      await message.channel.send(random.choice(spidey_gif))
    
    if message.content.startswith('*spideyquotes'):
      await message.channel.send(random.choice(spidey_quotes))

          
    #antman
    if message.content.startswith('*antmangif'):
      await message.channel.send(random.choice(antman_gif))
    
    if message.content.startswith('*antmanquotes'):
      await message.channel.send(random.choice(antman_quotes))


    #rhodes
    if message.content.startswith('*rhodesgif'):
      await message.channel.send(random.choice(rhodes_gif))
    
    if message.content.startswith('*rhodesquotes'):
      await message.channel.send(random.choice(rhodes_quotes))


    #Cap Marvel
    if message.content.startswith('*capmarvelgif'):
      await message.channel.send(random.choice(capmarvel_gif))
    
    if message.content.startswith('*capmarvelquotes'):
      await message.channel.send(random.choice(capmarvel_quotes))
    
    
   
    #wong
    if message.content.startswith('*wonggif'):
      await message.channel.send(random.choice(wong_gif))
    
    if message.content.startswith('*wongquotes'):
      await message.channel.send(random.choice(wong_quotes))


    #happy
    if message.content.startswith('*happygif'):
      await message.channel.send('Here is the help!')
    
    if message.content.startswith('*happyquotes'):
      await message.channel.send('Here is the help!')


    #Rocket
    if message.content.startswith('*rocketgif'):
      await message.channel.send('Here is the help!')
    
    if message.content.startswith('*rocketquotes'):
      await message.channel.send('Here is the help!')


    #Star Lord
    if message.content.startswith('*starlordgif'):
      await message.channel.send('Here is the help!')
    
    if message.content.startswith('*starlordquotes'):
      await message.channel.send('Here is the help!')


    #Pepper Potts
    if message.content.startswith('*peppergif'):
      await message.channel.send('Here is the help!')
    
    if message.content.startswith('*pepperquotes'):
      await message.channel.send('Here is the help!')


    #thanos
    if message.content.startswith('*thanosgif'):
      await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*thanosquotes'):
    #  await message.channel.send('Here is the help!')


    #Dr Strange
   # if message.content.startswith('*drstrangegif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('drstrangequotes'):
   #   await message.channel.send('Here is the help!')

    
    #Black Panther
  #  if message.content.startswith('*blackpanthergif'):
    #  await message.channel.send('Here is the help!')
   # 
   # if message.content.startswith('*blackpantherquotes'):
    #  await message.channel.send('Here is the help!')




    #Gamora
  #  if message.content.startswith('*gamoragif'):
   #   await message.channel.send('Here is the help!')
    
  #  if message.content.startswith('*gamoraquotes'):
   #   await message.channel.send('Here is the help!')


    #Wanda
  #  if message.content.startswith('*wandagif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*wandaquotes'):
   #   await message.channel.send('Here is the help!')


    #Vision
  #  if message.content.startswith('*visiongif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('visionquotes'):
   #   await message.channel.send('Here is the help!')


    #Falcon
  #  if message.content.startswith('*falcongif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*falconquotes'):
    #  await message.channel.send('Here is the help!')


 

    #Mantis
   # if message.content.startswith('*mantisgif'):
  #    await message.channel.send('Here is the help!')
    
  #  if message.content.startswith('*mantisquotes'):
  #    await message.channel.send('Here is the help!')


    #Drax
  #  if message.content.startswith('*draxgif'):
  #    await message.channel.send('Here is the help!')
    
  #  if message.content.startswith('*draxquotes'):
  #    await message.channel.send('Here is the help!')


    #Shuri
  #  if message.content.startswith('*shurigif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*shuriquotes'):
    #  await message.channel.send('Here is the help!')


    #Maria Hill
   # if message.content.startswith('*mariahillgif'):
   #   await message.channel.send('Here is the help!')
    
  #  if message.content.startswith('*mariahillquotes'):
    #  await message.channel.send('Here is the help!')


    #Ned
   # if message.content.startswith('*nedgif'):
   #   await message.channel.send('Here is the help!')
    
  #  if message.content.startswith('*nedquotes'):
     # await message.channel.send('Here is the help!')


    #Groot
   # if message.content.startswith('*grootgif'):
    #  await message.channel.send('Here is the help!')
    
    #if message.content.startswith('*grootquotes'):
   #   await message.channel.send('Here is the help!')


    #Fury
  #  if message.content.startswith('*furygif'):
 #     await message.channel.send('Here is the help!')
    
#    if message.content.startswith('*furyquotes'):
    #  await message.channel.send('Here is the help!')


    #MBaku
   # if message.content.startswith('*mbakugif'):
  #    await message.channel.send('Here is the help!')
    
    #if message.content.startswith('*mbakuquotes'):
   #   await message.channel.send('Here is the help!')


    #Ebony Maw
   # if message.content.startswith('*ebonymawgif'):
  #    await message.channel.send('Here is the help!')
    
 #   if message.content.startswith('*ebonymawquotes'):
    #  await message.channel.send('Here is the help!')

    #Val
   # if message.content.startswith('*valgif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*valquotes'):
   #   await message.channel.send('Here is the help!')


    #Ancient one
    #if message.content.startswith('*ancientonegif'):
     # await message.channel.send('Here is the help!')
    #
    #if message.content.startswith('*ancientonequotes'):
     # await message.channel.send('Here is the help!')


    #Peggy
    #if message.content.startswith('*peggygif'):
    #  await message.channel.send('Here is the help!')
    
   # if message.content.startswith('*peggyquotes'):
   #   await message.channel.send('Here is the help!')


 

    
    #Hank Pym
    #if message.content.startswith('*hankpymgif'):
   #   await message.channel.send('Here is the help!')
  #  
 #   if message.content.startswith('*hankpymquotes'):
#      await message.channel.send('Here is the help!')

      
    #StanLee
    #await message.channel.send('Here is the help!')
    
    #if message.content.startswith('*stanleequotes'):
      #await message.channel.send('Here is the help!')

      
      

    

  

    

  
keep_alive()
client.run(os.getenv('TOKEN'))
