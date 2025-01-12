import string

def synonym_check(text):

    table = str.maketrans('', '', string.punctuation)
    text = text.translate(table)
    text = text.lower()


    synonyms = {
        'sad' : ["sad", "upset", "broken", "depressed", "sadness", "depressing", "saddened", "unhappy", "sorrowful", "dejected", "regretful", "mournful", "gloomy", "melancholy", "woeful",
                    "miserable", "doleful", "downcast", "despondent", "disconsolate", "downhearted", "crestfallen", "blue", "dismal",
                    "heartbroken", "depressed", "low", "dispirited", "discouraged", "demoralized", "desolate", "hopeless", "downtrodden"],

        'anxious' : ["anxious", "anxiety", "doubt", "doubtful", "doubting", "fear", "scared", "doubt", "nervous", "uneasy", "apprehensive", "worried", "worry", "tense",
                                    "frightened", "afraid", "terrified", "alarmed", "panicked", "panic", "dread", "terror", "phobia", "horror", "fright",
                                    "skeptical", "uncertain", "hesitant", "wary", "questioning"],

        'tempted' : ["addict", "porn", "pornography", "drinking", "alcohol", "drug",
                        "temptation", "tempt", "tempted", "addicted", "addiction", "enticed", "allured", "attracted", "drawn", "inclined",
                        "persuaded", "seduced", "lured", "provoked", "motivated", "swayed", "compelled"],

        'pride' : ["pride", "pridefulness", "prideful" "boastful", "boast", "boasting", "proud"],

        'anger' : ["mad", "madness", "anger", "angry", "rage", "fury", "ire", "wrath", "outrage", "resentment", "indignation", "irritation", "irritated", "grudge", "pissed", "annoyance", "annoying" "exasperation", "frustration", "frustrated",
                        "vexation", "displeasure", "hostility", "hostile", "temper", "fuming", "discontent", "bitter", "discontent", "antagonism", "enraging", "outrage", "outraging", "outrageous"]
    }

    matched_list = []

    for word in text.split():
        for list_name, synonym_list in synonyms.items():
            if word in synonym_list:
                matched_list.append(list_name)

    if not matched_list:
        return "error"

    return matched_list


def image_find(reference):
    books_by_author = {
        'David': ['Psalm'],
        'Isaiah': ['Isaiah'],
        'James': ['James'],
        'John': ['John', 'Revelation'],
        'Joshua': ['Joshua'],
        'Matthew': ['Matthew'],
        'Moses': ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy'],
        'Paul': ['Philippians', 'Hebrews', 'Timothy', 'Corinthians', 'Galatians', 'Ephesians'],
        'Peter': ['Peter'],
        'Solomon': ['Proverbs', 'Ecclesiastes']
    }

    book_name = ""
    reference_parts = reference.split()
    for part in reference_parts:
        if part.isdigit() or part.replace(":", "").isdigit():
            continue
        book_name = book_name + (part + " ")
    book_name = book_name.strip()

    for author, books in books_by_author.items():
        if book_name in books:
            return author

def popup_info(author):
        author_info = {
        "david": "David is renowned for his multifaceted role as a shepherd, warrior, and king of Israel. As a young shepherd, he famously defeated Goliath, a giant Philistine warrior, with a sling and a stone, which marked the beginning of his rise to prominence. David's reign is noted for uniting the tribes of Israel and establishing Jerusalem as his capital and spiritual center, where he brought the Ark of the Covenant. He wrote many psalms, reflecting his deep spirituality and complex human emotions.",
        "isaiah": "Isaiah is a pivotal prophet in the Bible, renowned for his deep spiritual insights, poetic prophecies during a turbulent period in Judah's history, and authoring the book of Isaiah. His messages in the Book of Isaiah emphasize repentance, hope, and divine justice, forecasting the coming of the Messiah which we now know is Jesus of Nazareth. Isaiah's influence extends across religious traditions, shaping theological concepts of redemption and divine sovereignty.",
        "james": "James, a Christian Apostle and brother of Jesus of Nazareth, authored the book of James. James was not a follower or believer in his brother's ministry. After the resurrection event, he converted and became an important leader of the Jerusalem church. James was martyred around 62 AD, thrown from the Temple's pinnacle and then clubbed to death.",
        "john": "John was one of Jesus's closest disciples and he wrote the Gospel of John, three epistles, and the Book of Revelation. John's writings emphasize the divinity of Christ and the nature of God as love. John miraculously survived being boiled in oil at the hands of Roman authorities in Rome. Despite this attempt on his life, John died of natural causes in Ephesus, making him the only one of the original apostles not to die a martyr's death.",
        "joshua": "Joshua was Moses' assistant and led the Israelites to the Promised Land of Canaan after Moses' death. As a military leader, Joshua conquered and allocated the land among the twelve trives of Israel. He wrote the Book of Joshua, which emphasizes his faithfulness and obedience to God.",
        "matthew": "Before becoming a disciple of Jesus Christ, Matthew was a tax collector and was despised by his own Jewish people for his association with Roman oppression. He authored the Book of Matthew which documents the teachings of Jesus and fulfillment of Old Testament prophecies. Matthew was killed by a sword wound in Ethiopia.",
        "moses": "Moses is revered as a prophet, leader, and lawgiver in the Bible. He led the Israelites out of Egyptian slavery, crossed the Red Sea with the power of God, and received the Ten Commandments from God on Mount Sinai. Moses wrote the first five books of the Bible: Genesis, Exodus, Leviticus, Deuteronomy.",
        "paul": "Paul was originally known as Saul of Tarsus. Before his conversion on the road to Damascus, he was a zealous Pharisee who persecuted and killed Christians. After his encounter with the risen Jesus, Paul devoted his life to spreading the teachings of Jesus, establishing Christian communities and writing letters to various churches (which are now found in the New Testament). In AD 67, Paul was tortured and beheaded by order of Emperor Nero in Rome.",
        "peter": "Peter, originally named Simon, was one of the 12 disciples of Jesus Christ and wrote the Book of Peter. Known for his implulsive nature and deep faith, he was designated by Jesus as the 'rock' upon which the Church would be built. After Jesus' resurrection, Peter took a leading role in spreading the Gospel. Peter met his martyrdom in Rome around AD 64, crucified uspside down at his own request, feeling unworthy to die in the same manner as Jesus.",
        "solomon": "Solomon, son of King David, is renowned for his wisdom, wealth, and building projects. He constructed the First Temple in Jerusalem which solidified the city as the center of Israel. His reign was charactertized by peace and prosperity. Solomon authored Proverbs and Ecclesiastes which include philosophy, ethics, and the complexities of human life."
    }
        return author_info.get(author, "Author not found")
