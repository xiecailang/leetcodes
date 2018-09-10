'''
贝叶斯
好评：{"high cost performance","Great place","Have a good time","quite special","good place","easy of access","Very worth a visit", "tickets are cheap", "convenient traffic", "overall feels good", "worth to see", "very convenient traffic", "very fun", "a good place", "The ticket is cost-effective", "the overall feeling is good", "the place worth going", "the view is good", "the overall is not bad", "feel good", "the scenery is very good", "the scenery is not bad", "I like it very much", "Really good", "It's worth seeing", "The ticket is not expensive", "The ticket is very cheap", "The scenery is not bad", "The price is very good", "It's still very good", "The scenery is very good", "The environment is great", "The scenery is OK", "The air is very fresh", "Very worth seeing", "Very worth going", "Good view", "Good traffic"," Value this price", "good value for money"}
差评：{"low cost performance", "I don't prefer it", "Nothing fun", "Nothing special", "Nothing good-looking", "Traffic is not very convenient", "Nothing special", "Tickets are too expensive", "Traffic inconvenient", "The overall feeling is bad", "Nothing to play", "Never come again", "Nothing to see", "Feeling bad", "Tickets are a bit expensive", "very bad", "The scenery is bad", "There is nothing to watch", "I don't like it", "The price is a bit expensive", "cost performance is too low", "I feel not good", "not high cost performance", "Not very fun", "Tickets are not cheap ", "traffic is not convenient", "the scenery is not good", "nothing to play", "too commercial", "tickets are expensive", "fare is a bit expensive", "nothing to see", "price not cheap", "price is very high", "ticket too expensive", "The traffic is not good", "The ticket is too expensive", "The scenery is very poor", "Not worth the price", "The traffic is bad"}
'''
good_ = [strs.lower() for strs in ["high cost performance","Great place","Have a good time","quite special","good place","easy of access","Very worth a visit", "tickets are cheap", "convenient traffic", "overall feels good", "worth to see", "very convenient traffic", "very fun", "a good place", "The ticket is cost-effective", "the overall feeling is good", "the place worth going", "the view is good", "the overall is not bad", "feel good", "the scenery is very good", "the scenery is not bad", "I like it very much", "Really good", "It's worth seeing", "The ticket is not expensive", "The ticket is very cheap", "The scenery is not bad", "The price is very good", "It's still very good", "The scenery is very good", "The environment is great", "The scenery is OK", "The air is very fresh", "Very worth seeing", "Very worth going", "Good view", "Good traffic"," Value this price", "good value for money"]]
bad_ = [strs.lower() for strs in ["low cost performance", "I don't prefer it", "Nothing fun", "Nothing special", "Nothing good-looking", "Traffic is not very convenient", "Nothing special", "Tickets are too expensive", "Traffic inconvenient", "The overall feeling is bad", "Nothing to play", "Never come again", "Nothing to see", "Feeling bad", "Tickets are a bit expensive", "very bad", "The scenery is bad", "There is nothing to watch", "I don't like it", "The price is a bit expensive", "cost performance is too low", "I feel not good", "not high cost performance", "Not very fun", "Tickets are not cheap ", "traffic is not convenient", "the scenery is not good", "nothing to play", "too commercial", "tickets are expensive", "fare is a bit expensive", "nothing to see", "price not cheap", "price is very high", "ticket too expensive", "The traffic is not good", "The ticket is too expensive", "The scenery is very poor", "Not worth the price", "The traffic is bad"]]

new_words = [strs.lower() for strs in input().split()]
good_prs = []
bad_prs = []
for w in new_words:
    good_pr = sum([1 if w in strs else 0 for strs in good_])/len(good_)
    if good_pr == 0:
        good_pr = 0.01 
    good_prs.append(good_pr)
    bad_pr = sum([1 if w in strs else 0 for strs in bad_])/len(bad_)
    if bad_pr == 0:
        bad_pr = 0.01 
    bad_prs.append(bad_pr)
p_G, p_B = 0.5, 0.5 #好评差评的概率
from functools import reduce
ans_p_good = reduce(lambda x,y:x*y, good_prs) * p_G
ans_p_bad = reduce(lambda x,y:x*y, bad_prs) * p_B
print('good' if ans_p_good > ans_p_bad else 'bad')



