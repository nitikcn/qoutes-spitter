#! /bin/env python3

import random

def get_quote():
    return random.choice(QUOTES)

QUOTES = ['If you want to achieve greatness stop asking for permission.\n-- Anonymous',
 'Things work out best for those who make the best of how things work out.\n'
 '-- John Wooden',
 'To live a creative life, we must lose our fear of being wrong.\n-- Anonymous',
 'If you are not willing to risk the usual you will have to settle for the '
 'ordinary.\n'
 '-- Jim Rohn',
 "Trust because you are willing to accept the risk, not because it's safe or "
 'certain.\n'
 '-- Anonymous',
 'Take up one idea. Make that one idea your life - think of it, dream of it, '
 'live on that idea. Let the brain, muscles, nerves, every part of your body, '
 'be full of that idea, and just leave every other idea alone. This is the way '
 'to success.\n'
 '-- Swami Vivekananda',
 'All our dreams can come true if we have the courage to pursue them.\n'
 '-- Walt Disney',
 'Good things come to people who wait, but better things come to those who go '
 'out and get them.\n'
 '-- Anonymous',
 'If you do what you always did, you will get what you always got.\n'
 '-- Anonymous',
 'Success is walking from failure to failure with no loss of enthusiasm.\n'
 '-- Winston Churchill',
 'Just when the caterpillar thought the world was ending, he turned into a '
 'butterfly.\n'
 '-- Proverb',
 'Successful entrepreneurs are givers and not takers of positive energy.\n'
 '-- Anonymous',
 'Whenever you see a successful person you only see the public glories, never '
 'the private sacrifices to reach them.\n'
 '-- Vaibhav Shah',
 "Opportunities don't happen, you create them.\n-- Chris Grosser",
 'Try not to become a person of success, but rather try to become a person of '
 'value.\n'
 '-- Albert Einstein',
 'Great minds discuss ideas; average minds discuss events; small minds discuss '
 'people.\n'
 '-- Eleanor Roosevelt',
 "I have not failed. I've just found 10,000 ways that won't work.\n"
 '-- Thomas A. Edison',
 "If you don't value your time, neither will others. Stop giving away your "
 'time and talents- start charging for it.\n'
 '-- Kim Garst',
 'A successful man is one who can lay a firm foundation with the bricks others '
 'have thrown at him.\n'
 '-- David Brinkley',
 'No one can make you feel inferior without your consent.\n'
 '-- Eleanor Roosevelt',
 "The whole secret of a successful life is to find out what is one's destiny "
 'to do, and then do it.\n'
 '-- Henry Ford',
 "If you're going through hell keep going.\n-- Winston Churchill",
 'The ones who are crazy enough to think they can change the world, are the '
 'ones that do.\n'
 '-- Anonymous',
 "Don't raise your voice, improve your argument.\n-- Anonymous",
 'What seems to us as bitter trials are often blessings in disguise.\n'
 '-- Oscar Wilde',
 'The meaning of life is to find your gift. The purpose of life is to give it '
 'away.\n'
 '-- Anonymous',
 'The distance between insanity and genius is measured only by success.\n'
 '-- Bruce Feirstein',
 'When you stop chasing the wrong things you give the right things a chance to '
 'catch you.\n'
 '-- Lolly Daskal',
 "Don't be afraid to give up the good to go for the great.\n"
 '-- John D. Rockefeller',
 'No masterpiece was ever created by a lazy artist.\n-- Anonymous',
 'Happiness is a butterfly, which when pursued, is always beyond your grasp, '
 'but which, if you will sit down quietly, may alight upon you.\n'
 '-- Nathaniel Hawthorne',
 "If you can't explain it simply, you don't understand it well enough.\n"
 '-- Albert Einstein',
 'Blessed are those who can give without remembering and take without '
 'forgetting.\n'
 '-- Anonymous',
 'Do one thing every day that scares you.\n-- Anonymous',
 "What's the point of being alive if you don't at least try to do something "
 'remarkable.\n'
 '-- Anonymous',
 'Life is not about finding yourself. Life is about creating yourself.\n'
 '-- Lolly Daskal',
 'Nothing in the world is more common than unsuccessful people with talent.\n'
 '-- Anonymous',
 'Knowledge is being aware of what you can do. Wisdom is knowing when not to '
 'do it.\n'
 '-- Anonymous',
 "Your problem isn't the problem. Your reaction is the problem.\n-- Anonymous",
 'You can do anything, but not everything.\n-- Anonymous',
 'Innovation distinguishes between a leader and a follower.\n-- Steve Jobs',
 'There are two types of people who will tell you that you cannot make a '
 'difference in this world: those who are afraid to try and those who are '
 'afraid you will succeed.\n'
 '-- Ray Goforth',
 'Thinking should become your capital asset, no matter whatever ups and downs '
 'you come across in your life.\n'
 '-- Dr. APJ Kalam',
 'I find that the harder I work, the more luck I seem to have.\n'
 '-- Thomas Jefferson',
 'The starting point of all achievement is desire.\n-- Napolean Hill',
 'Success is the sum of small efforts, repeated day-in and day-out.\n'
 '-- Robert Collier',
 'If you want to achieve excellence, you can get there today. As of this '
 'second, quit doing less-than-excellent work.\n'
 '-- Thomas J. Watson',
 'All progress takes place outside the comfort zone.\n-- Michael John Bobak',
 'You may only succeed if you desire succeeding; you may only fail if you do '
 'not mind failing.\n'
 '-- Philippos',
 'Courage is resistance to fear, mastery of fear - not absense of fear.\n'
 '-- Mark Twain',
 'Only put off until tomorrow what you are willing to die having left undone.\n'
 '-- Pablo Picasso',
 "People often say that motivation doesn't last. Well, neither does bathing - "
 "that's why we recommend it daily.\n"
 '-- Zig Ziglar',
 "We become what we think about most of the time, and that's the strangest "
 'secret.\n'
 '-- Earl Nightingale',
 'The only place where success comes before work is in the dictionary.\n'
 '-- Vidal Sassoon',
 'The best reason to start an organization is to make meaning; to create a '
 'product or service to make the world a better place.\n'
 '-- Guy Kawasaki',
 'I find that when you have a real interest in life and a curious life, that '
 'sleep is not the most important thing.\n'
 '-- Martha Stewart',
 "It's not what you look at that matters, it's what you see.\n-- Anonymous",
 'The road to success and the road to failure are almost exactly the same.\n'
 '-- Colin R. Davis',
 'The function of leadership is to produce more leaders, not more followers.\n'
 '-- Ralph Nader',
 'Success is liking yourself, liking what you do, and liking how you do it.\n'
 '-- Maya Angelou',
 'As we look ahead into the next century, leaders will be those who empower '
 'others.\n'
 '-- Bill Gates',
 'A real entrepreneur is somebody who has no safety net underneath them.\n'
 '-- Henry Kravis',
 'The first step toward success is taken when you refuse to be a captive of '
 'the environment in which you first find yourself.\n'
 '-- Mark Caine',
 'People who succeed have momentum. The more they succeed, the more they want '
 'to succeed, and the more they find a way to succeed. Similarly, when someone '
 'is failing, the tendency is to get on a downward spiral that can even become '
 'a self-fulfilling prophecy.\n'
 '-- Tony Robbins',
 'When I dare to be powerful - to use my strength in the service of my vision, '
 'then it becomes less and less important whether I am afraid.\n'
 '-- Audre Lorde',
 'Whenever you find yourself on the side of the majority, it is time to pause '
 'and reflect.\n'
 '-- Mark Twain',
 'The successful warrior is the average man, with laser-like focus.\n'
 '-- Bruce Lee',
 'Take up one idea. Make that one idea your life -- think of it, dream of it, '
 'live on that idea. Let the brain, muscles, nerves, every part of your body, '
 'be full of that idea, and just leave every other idea alone. This is the way '
 'to success.\n'
 '-- Swami Vivekananda',
 'Develop success from failures. Discouragement and failure are two of the '
 'surest stepping stones to success.\n'
 '-- Dale Carnegie',
 "If you don't design your own life plan, chances are you'll fall into someone "
 "else's plan. And guess what they have planned for you? Not much.\n"
 '-- Jim Rohn',
 "If you genuinely want something, don't wait for it -- teach yourself to be "
 'impatient.\n'
 '-- Gurbaksh Chahal',
 "Don't let the fear of losing be greater than the excitement of winning.\n"
 '-- Robert Kiyosaki',
 'If you want to make a permanent change, stop focusing on the size of your '
 'problems and start focusing on the size of you!\n'
 '-- T. Harv Eker',
 "You can't connect the dots looking forward; you can only connect them "
 'looking backwards. So you have to trust that the dots will somehow connect '
 'in your future. You have to trust in something - your gut, destiny, life, '
 'karma, whatever. This approach has never let me down, and it has made all '
 'the difference in my life.\n'
 '-- Steve Jobs',
 "Successful people do what unsuccessful people are not willing to do. Don't "
 'wish it were easier, wish you were better.\n'
 '-- Jim Rohn',
 'The number one reason people fail in life is because they listen to their '
 'friends, family, and neighbors.\n'
 '-- Napoleon Hill',
 "The reason most people never reach their goals is that they don't define "
 'them, or ever seriously consider them as believable or achievable. Winners '
 'can tell you where they are going, what they plan to do along the way, and '
 'who will be sharing the adventure with them.\n'
 '-- Denis Watiley',
 'In my experience, there is only one motivation, and that is desire. No '
 'reasons or principle contain it or stand against it.\n'
 '-- Jane Smiley',
 'Success does not consist in never making mistakes but in never making the '
 'same one a second time.\n'
 '-- George Bernard Shaw',
 "I don't want to get to the end of my life and find that I lived just the "
 'length of it. I want to have lived the width of it as well.\n'
 '-- Diane Ackerman',
 'You must expect great things of yourself before you can do them.\n'
 '-- Michael Jordan',
 'Motivation is what gets you started. Habit is what keeps you going.\n'
 '-- Jim Ryun',
 'People rarely succeed unless they have fun in what they are doing.\n'
 '-- Dale Carnegie',
 'There is no chance, no destiny, no fate, that can hinder or control the firm '
 'resolve of a determined soul.\n'
 '-- Ella Wheeler Wilcox',
 'Our greatest fear should not be of failure but of succeeding at things in '
 "life that don't really matter.\n"
 '-- Francis Chan',
 "You've got to get up every morning with determination if you're going to go "
 'to bed with satisfaction.\n'
 '-- George Lorimer',
 'To be successful you must accept all challenges that come your way. You '
 "can't just accept the ones you like.\n"
 '-- Mike Gafka',
 'Success is...knowing your purpose in life, growing to reach your maximum '
 'potential, and sowing seeds that benefit others.\n'
 '-- John C. Maxwell',
 "Be miserable. Or motivate yourself. Whatever has to be done, it's always "
 'your choice.\n'
 '-- Wayne Dyer',
 'To accomplish great things, we must not only act, but also dream, not only '
 'plan, but also believe.\n'
 '-- Anatole France',
 'Most of the important things in the world have been accomplished by people '
 'who have kept on trying when there seemed to be no help at all.\n'
 '-- Dale Carnegie',
 'You measure the size of the accomplishment by the obstacles you had to '
 'overcome to reach your goals.\n'
 '-- Booker T. Washington',
 'Real difficulties can be overcome; it is only the imaginary ones that are '
 'unconquerable.\n'
 '-- Theodore N. Vail',
 'It is better to fail in originality than to succeed in imitation.\n'
 '-- Herman Melville',
 'Fortune sides with him who dares.\n-- Virgil',
 'Little minds are tamed and subdued by misfortune; but great minds rise above '
 'it.\n'
 '-- Washington Irving',
 'Failure is the condiment that gives success its flavor.\n-- Truman Capote',
 "Don't let what you cannot do interfere with what you can do.\n"
 '-- John R. Wooden',
 'You may have to fight a battle more than once to win it.\n'
 '-- Margaret Thatcher']

if __name__ == '__main__':
    print(get_quote())
