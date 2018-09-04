'''
贝叶斯
好评：{"high cost performance","Great place","Have a good time","quite special","good place","easy of access","Very worth a visit", "tickets are cheap", "convenient traffic", "overall feels good", "worth to see", "very convenient traffic", "very fun", "a good place", "The ticket is cost-effective", "the overall feeling is good", "the place worth going", "the view is good", "the overall is not bad", "feel good", "the scenery is very good", "the scenery is not bad", "I like it very much", "Really good", "It's worth seeing", "The ticket is not expensive", "The ticket is very cheap", "The scenery is not bad", "The price is very good", "It's still very good", "The scenery is very good", "The environment is great", "The scenery is OK", "The air is very fresh", "Very worth seeing", "Very worth going", "Good view", "Good traffic"," Value this price", "good value for money"}
差评：{"low cost performance", "I don't prefer it", "Nothing fun", "Nothing special", "Nothing good-looking", "Traffic is not very convenient", "Nothing special", "Tickets are too expensive", "Traffic inconvenient", "The overall feeling is bad", "Nothing to play", "Never come again", "Nothing to see", "Feeling bad", "Tickets are a bit expensive", "very bad", "The scenery is bad", "There is nothing to watch", "I don't like it", "The price is a bit expensive", "cost performance is too low", "I feel not good", "not high cost performance", "Not very fun", "Tickets are not cheap ", "traffic is not convenient", "the scenery is not good", "nothing to play", "too commercial", "tickets are expensive", "fare is a bit expensive", "nothing to see", "price not cheap", "price is very high", "ticket too expensive", "The traffic is not good", "The ticket is too expensive", "The scenery is very poor", "Not worth the price", "The traffic is bad"}
'''
good_ = ["high cost performance","Great place","Have a good time","quite special","good place","easy of access","Very worth a visit", "tickets are cheap", "convenient traffic", "overall feels good", "worth to see", "very convenient traffic", "very fun", "a good place", "The ticket is cost-effective", "the overall feeling is good", "the place worth going", "the view is good", "the overall is not bad", "feel good", "the scenery is very good", "the scenery is not bad", "I like it very much", "Really good", "It's worth seeing", "The ticket is not expensive", "The ticket is very cheap", "The scenery is not bad", "The price is very good", "It's still very good", "The scenery is very good", "The environment is great", "The scenery is OK", "The air is very fresh", "Very worth seeing", "Very worth going", "Good view", "Good traffic"," Value this price", "good value for money"]
bad_ = ["low cost performance", "I don't prefer it", "Nothing fun", "Nothing special", "Nothing good-looking", "Traffic is not very convenient", "Nothing special", "Tickets are too expensive", "Traffic inconvenient", "The overall feeling is bad", "Nothing to play", "Never come again", "Nothing to see", "Feeling bad", "Tickets are a bit expensive", "very bad", "The scenery is bad", "There is nothing to watch", "I don't like it", "The price is a bit expensive", "cost performance is too low", "I feel not good", "not high cost performance", "Not very fun", "Tickets are not cheap ", "traffic is not convenient", "the scenery is not good", "nothing to play", "too commercial", "tickets are expensive", "fare is a bit expensive", "nothing to see", "price not cheap", "price is very high", "ticket too expensive", "The traffic is not good", "The ticket is too expensive", "The scenery is very poor", "Not worth the price", "The traffic is bad"]
good_words = [n for a in [str_.split() for str_ in good_] for n in a]
bad_words = [n for a in [str_.split() for str_ in bad_] for n in a]
good_keys = list(set(good_words))
bad_keys = list(set(bad_words))
p_good = {}
p_bad = {}
#计算概率
for w in good_keys:
    p_good[w] = good_words.count(w)/len(good_words)
for w in bad_keys:
    p_bad[w] = bad_words.count(w)/len(good_words)
target = input().split()
p_g, p_b = 0, 0
for w in target:
    if w in p_good:
        p_g += p_good[w]
    if w in p_bad:
        p_b += p_bad[w]
print(1 if p_g>p_b else 0)
