from helpers import *

data = get_data(100000)

dead_words = ["awesome", "cool", "awful", "fun", "funny", "good", "great", "mad", "nice", "pretty", "scared", "very", "really", "quite"]
dead_reviews = dead_word_filter(dead_words, data)

short_reviews = len_filter(20, data)

unhelpful_reviews = helpfulness_filter(0.5, data)

perf_imperf_reviews = perfection_filter(data)

validity5_reviews = validity_filter(5, data)
validity4_reviews = validity_filter(4, data)
validity3_reviews = validity_filter(3, data)
validity2_reviews = validity_filter(2, data)
validity1_reviews = validity_filter(1, data)

print()
print("Random DEAD review:")
i = random.randrange(len(dead_reviews))
dead_reviews[i].print()

print()
print("Random SHORT review:")
i = random.randrange(len(short_reviews))
short_reviews[i].print()

print()
print("Random UNHELPFUL review:")
i = random.randrange(len(unhelpful_reviews))
unhelpful_reviews[i].print()

print()
print("Random PERFECT/IMPERFECT review:")
i = random.randrange(len(perf_imperf_reviews))
perf_imperf_reviews[i].print()

print()
print("Random 5 Validity Score review:")
i = random.randrange(len(validity5_reviews))
validity5_reviews[i].print()

print()
print("Random 4 Validity Score review:")
i = random.randrange(len(validity4_reviews))
validity4_reviews[i].print()

print()
print("Random 3 Validity Score review:")
i = random.randrange(len(validity3_reviews))
validity3_reviews[i].print()

print()
print("Random 2 Validity Score review:")
i = random.randrange(len(validity2_reviews))
validity2_reviews[i].print()

print()
print("Random 1 Validity Score review:")
i = random.randrange(len(validity1_reviews))
validity1_reviews[i].print()
