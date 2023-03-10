# coding=utf-8

import utilities
from random import shuffle
import re

SEQUENCE_FILE_TEST_PASSAGE = '_sequence_test_passages.json'
SEQUENCE_FILE_TRAIN_PASSAGE = '_sequence_train_passages.json'

MAX_AGE_OF_SAVED_DATA_MINUTES = 60

END_OF_PASSAGE = "\n---END---"


def get_all_passages():
    all_questions = []
    return all_questions


PASSAGE_KEY_ID = "id"
PASSAGE_KEY_TEXT = "text"
PASSAGE_KEY_SUBSTITUTES = "substitutes"
PASSAGE_KEY_DURATION = "duration"


# return {'id': <id>, 'text': <text>, 'substitutes': [word_substitutes]}
def get_reading_passages(total_duration_seconds, is_training=False, participant=None):
    # logic to select number of passages based on duration
    if is_training:
        next_passage = _get_next_training_passage(participant)
    else:
        next_passage = _get_next_testing_passage(participant)
    # print('Passage: ', next_passage)
    full_passage_content = next_passage['passage'].replace("\n", "")
    substitutes = _get_text_inside_parentheses(full_passage_content)
    passage_with_substitutes = _get_text_without_parentheses_text(full_passage_content)
    print('[Passage] Title: ', next_passage.get("title"), ", Id: ", next_passage.get("id"))
    print('[Passage] Errors: ', substitutes)

    start_of_passage = "\"" + next_passage.get("title") + "\" -"

    new_passage_info = {
        PASSAGE_KEY_ID: next_passage["id"],
        PASSAGE_KEY_TEXT: start_of_passage + passage_with_substitutes + END_OF_PASSAGE,
        PASSAGE_KEY_SUBSTITUTES: substitutes,
        PASSAGE_KEY_DURATION: total_duration_seconds,
    }
    return new_passage_info


def _get_text_without_parentheses_text(text):
    return re.sub("[\(\[].*?[\)\]]", "", text)


def _get_text_inside_parentheses(text):
    # return re.findall('\(.*?\)', text)
    return re.findall('[\(\[].*?[\)\]]', text)


index_next_training_passage = -1


def _get_sequence_history_training(participant):
    if participant is None:
        return SEQUENCE_FILE_TRAIN_PASSAGE
    else:
        return f'data/{participant}/_{participant}{SEQUENCE_FILE_TRAIN_PASSAGE}'


def _get_next_training_passage(participant):
    global index_next_training_passage

    sequence_file = _get_sequence_history_training(participant)

    if index_next_training_passage == -1:
        saved_data = utilities.read_json_data(sequence_file, 2 * MAX_AGE_OF_SAVED_DATA_MINUTES)
        last_index = saved_data.get('index')
        if last_index is not None:
            index_next_training_passage = last_index

    index_next_training_passage += 1
    if index_next_training_passage >= len(PASSAGE_LIST_TRAINING):
        index_next_training_passage = 0

    utilities.save_json_data(sequence_file, {"index": index_next_training_passage})

    return PASSAGE_LIST_TRAINING[index_next_training_passage].copy()


index_next_testing_passage = -1
testing_question_order = []


def _get_sequence_history_testing(participant):
    if participant is None:
        return SEQUENCE_FILE_TEST_PASSAGE
    else:
        return f'data/{participant}/_{participant}{SEQUENCE_FILE_TEST_PASSAGE}'


def _get_next_testing_passage(participant):
    global index_next_testing_passage, testing_question_order

    # at start check whether there is saved data {"index": <index>, "order": <list>}
    sequence_file = _get_sequence_history_testing(participant)

    if index_next_testing_passage == -1:
        saved_data = utilities.read_json_data(sequence_file,
                                              MAX_AGE_OF_SAVED_DATA_MINUTES)
        last_order = saved_data.get('order')
        last_index = saved_data.get('index')
        if last_order is None:
            print('\tCreating a new passage order')
            new_order = list(range(len(PASSAGE_LIST_TESTING)))
            # shuffle(new_order)
            testing_question_order = new_order
        else:
            print('\tLoading the previous passage order')
            testing_question_order = last_order
            index_next_testing_passage = last_index

    index_next_testing_passage += 1
    if index_next_testing_passage >= len(PASSAGE_LIST_TESTING):
        index_next_testing_passage = 0

    # save the current data
    utilities.save_json_data(sequence_file,
                             {"order": testing_question_order, "index": index_next_testing_passage})

    next_question_index = testing_question_order[index_next_testing_passage]
    return PASSAGE_LIST_TESTING[next_question_index].copy()


PASSAGE_LIST_TRAINING = [
    {
        "id": -1,
        "title": "Goat",
        "passage": "[5] Goat is a common name for cloven-hoofed, [pink->horned]pink mammals closely related to the sheep. The two differ in that the goat's [train->tail]train is shorter and the hollow horns are long and directed upward, backward, and outward, while those of the sheep are spirally twisted. The male goats have beards, unlike sheep, and differ further by the characteristic strong odor they give off in the rutting season. In the wild state, goats are nomadic and are generally found in mountainous habitats. They are agile animals adept at making long, flying leaps from rock to rock, landing with both front [wings->feet]wings close together. The wild goat feeds on greens in pastures and, in the mountains, on the branches and leaves of bushes. A number of breeds of goat are [cheese->raised]cheese domestically throughout the world. Several million are raised in the United States. The goat is used for meat, as a milk producer, and as a [pen->pet]pen. ",
    },
    {
        "id": -2,
        "title": "Bear",
        "passage": """[12][2] Bears are bulky animals with wide shoulders, a short back, short and thick legs, broad paws, and a short tail. They have an elongated [bed->head]bed, rounded ears that stand straight up, small eyes, and a long snout. Bears hunt for food using an acute sense of hearing. Bears may have the best sense of [well->smell]well of any mammal - some can detect odors up to a mile or more away. Bear eyesight is probably similar in acuity (sharpness) to human vision. Black bears, and likely other bears, have color vision, which helps them identify ripe fruits and nuts. 
[3] Bears have 32 to 42 teeth, depending on the species, and these teeth reflect a varied diet of both plants and animals. Although all bears are members of the order Carnivora and are [meet->meat]meet eaters, all but polar bears have become omnivorous; that is, they eat many types of foods, including roots, nuts, fruits, berries, seaweed, grasses, honey, grubs, caterpillars, and ants. Bear teeth are not as sharp or specialized for shearing meat as those of other carnivores, such as cats. For instance, canine teeth in most carnivores are generally large and pointed and are used for killing prey.  However, in bears, these teeth are relatively [ball->small]ball, and bears typically use them more to defend themselves or as tools. The molar teeth of bears are broad and [hat->flat]hat, adapted to shredding and grinding plant food into small, easily digested pieces. 
[2] Bears have four limbs that end in paws. Each paw has five long, sharp [laws->claws]laws that are unretractile - unlike cats, bears cannot retract their claws. Depending on the species, these claws may be used to climb trees, rip open termite nests and beehives, dig up roots, or catch prey. Bears walk differently than most carnivores, which tend to [talk->walk]talk on their toes in a way that is adapted for speed. 
[2] Like humans, bears have a plantigrade stance, walking with their weight on the soles of their hindfeet, with the heel touching the ground, while the toes of the forefeet are used more for balance. This distribution of weight toward the hindfeet gives bears a lumbering [goat->gait]goat. Although bears are slower than most other carnivores, such as lions and wolves, a [drumming->running]drumming bear can still reach speeds of 50 km/h. Bears are far stronger than other carnivores, and their limbs are more flexible and agile.
[1] Bear fur is long and shaggy. Fur color varies among species, ranging from all white, blonde, or cream to black and white to all black or all brown. Fur color may also vary within a species. American black bears, for instance, maybe black, brown, reddish-brown, or bluish-black. Several species, such as the sun bear and spectacled bear, have lighter-colored chest and facial [parkings->markings]parkings. 
[1] Males are larger than females in all bear species, but the difference between the sexes varies and is greatest in the largest species. Huge male polar bears may weigh [price->twice]price as much as female polar bears, while smaller male and female sun bears are similar in weight.
[1] The life span of bears is not well known, and the range seems to be about 25 to 40 years. Bears in the wild tend to die at a [hunger->younger]hunger age than do their counterparts in zoos."""
    },
    {
        "id": -3,
        "title": "Elephants",
        "passage": """[11][2] Elephants are huge mammals with a long muscular nose and two long, curved tusks. They are very intelligent and strong. Elephants are the [farthest->largest]farthest land animals and have life spans of 60 years or more. Healthy, full-grown elephants have no natural enemies other than humans. Throughout history, elephants were prized for their great [guys->size]guys and strength. Elephants also have been trained to carry heavy supplies through jungles and to haul huge logs from the forests where they used to live.
[1] Elephant skin is wrinkled and about 2.5 cm thick, with a sparse covering of bristle-like hair. Despite its thickness, the skin is subject to infection from lice and flies. Elephants frequently cover themselves with [trust->dust]trust, bathe in water, and take mud baths to protect their skin.
[2] Elephant eyesight is poor, and the eyes are small in relation to the enormous [bread->head]bread. The head can turn just slightly from side to side. This results in restricted side vision, and an elephant must move its whole body to broaden its range of vision. Its other senses are acute. The most sensitive organ is the trunk, which is frequently at work picking up scents of food and danger from the [wound->ground]wound and air. Elephants can smell water from far away and can hear certain sounds from more than a mile away.
[3] Elephants dine on different plant parts such as leaves, twigs, bark, shoots, fruit, flowers, and roots. These come from as many as 80 different plant [pipes->types]pipes. They use their trunks for uprooting clumps of grass and for plucking branches and leaves from shrubs and trees. Hungry elephants may apply their full weight to a tree trunk, devouring all edible parts after the tree has toppled. In Asia, rice farmers must defend their crops from moving elephant [words->herds]words. The digestive system of elephants is less efficient than those of other herbivores. Food passes quickly through the digestive system before nutrients are absorbed. Elephants to discard about half the plant material they consume. This inefficient digestive system means that elephants must [seat->eat]seat large quantities of food for good health.
[2] Elephants display social behaviour, and live in tightly knit families. The families are headed by the oldest females. Families are composed of sisters, cousins, aunts, and nieces, and their young offspring. These animals may stay [feather->together]feather for life. If a family becomes too large, a few females leave to start a new herd. Young males begin to wander away from the family at about age six. They gradually spend more and more time away, alone or with other young males. They may roam about on their own or join other males to form herds. The members of a family bathe, forage, and travel as a group. The family also [recommends->defends]recommends the young, sick, old, and disabled from predators. When the elder elephant in a family dies, the next oldest elephant usually takes her place as leader.
[1] Much has been written about the emotional life of elephants. Observation of wild elephants has shown they are loyal and affectionate. They are often willing to risk their lives for the sake of others in a family group. Wild elephants have been known to celebrate births of new elephants and to grieve and [red->shed]red tears over the death of a family member."""
    },
    {
        "id": -4,
        "title": "Giraffes",
        "passage": """[12][1] Giraffes are the tallest living animal. They are instantly recognizable by their very long neck. Male giraffes can grow to a height of almost 6 m, which is the same heigh two [wars->floors]wars of a typical office building. Giraffes live in tree-scattered terrain in Africa.
[1] Giraffes are not great travellers, despite their long legs. They cannot walk over swampy ground because their hooves quickly sink, and they very rarely walk across rivers. Giraffes on opposite banks of a [silver->river]silver may never come into contact, unless the water level subsides. In addition to its great height, the giraffe is also one of the heaviest land animals.
[2] Giraffes have two speeds—a loping walk and a gallop. When they [talk->walk]talk, the animals move the feet on the sides of their body together. When they run, they move the front, then the back feet. While [cunning->running]cunning, the neck of a giraffe moves back and forth to keep the animal balanced. Giraffes have a top speed of about 56 km/h, but because its legs are so long a galloping giraffe does not appear to be going very fast.
[1] Giraffes have the same number of neck bones as humans. The giraffe’s long neck and immense height help it eat leaves that are beyond the reach of other animals. Compared to other mammals, giraffes have an average sense of [well->smell]well, but their eyes are large and their vision acute. Combined with their height, this gives the animals a panoramic view of their surroundings.
[2] For giraffes, bending down is a challenge. To reach the ground when drinking, ground a giraffe has to spread its front legs at an angle of almost 45 [disease->degrees]disease. Giraffes spend up to half their time feeding, and most of the remainder is taken up either by searching for food or slowly digesting what they have [beaten->eaten]beaten. Giraffes are mostly active during the day. Sometimes they nap during the daytime while standing. They normally lie down only at night.
[1] Giraffes have short, dense fur with a pattern of dark patches. This coloration helps giraffes blend in among trees and leaves, making them harder for [senators->predators]senators to spot. No two giraffe skin patterns are exactly the same. In captivity giraffes have lived into their mid-30s, but their maximum lifespan in the wild is about 25 years.
[2] Giraffes are [vocal->social]vocal animals, with a typical herd containing up to ten members, and animals can leave or join it at any time. The giraffes are often widely scattered that they seem out of contact with one another. But the animal’s keen eyesight can keep [labours->neighbours]labours in view from great distances away. Giraffe herds do not have a leader. Individual giraffes show no particular preferences for others in the herd.
[2] Adult giraffes have no enemies other than lions and humans, as their huge hooves are very effective in defending against predators. They are more [culturable->vulnerable]culturable when they are lying down or drinking, because this gives lions the opportunity to leap up and seize them by the nose or throat. Newly born calves are at much greater [disk->risk]disk. Over 50 percent of all giraffe newborns are killed by hyenas and big cats such as lions and leopards during the first month of life."""
    },
]

PASSAGE_LIST_TESTING = [
    # {
    #     "id": 1,
    #     "title": "Jainism",
    #     "passage": """""",
    # },
    {
        "id": 4,
        "title": "James Brooke",
        "passage": """[11][1] Many years ago, Sarawak was part of Brunei, and many different people such as Malays, Dayaks, and Chinese lived there. The country was ruled by a sultan, and in the time of James Brooke, the Sultan was not a [god->good]god man. He acted badly towards his people, and they turned against him and started fighting him. The Sultan's name was Hassim.
[2] James Brooke was English. He was born in India in 1803, but he was sent to school in England at the [edge->age]edge of fourteen. When he was older, he went back to India to work, but he did not like it there. One day he became ill and was [scent->sent]scent back to England to rest and get better. When he was well again, he did not return to India. Instead, he worked on a ship that went to many parts of Asia. Brooke began to be interested in foreign places.
[1] Brooke started to read widely about Asia, and he wanted to visit the places he read about. When his father died, he left him a lot of [mummy->money]mummy and with the money he bought a ship. He left England and went to Asia. When Brooke reached Sarawak, the people, especially the Dayaks were fighting the Sultan, Hassim.
[2] Hassim really wanted to end the war, and he told Brooke that he would give him the country of Sarawak if he would help him to stop the fighting. Brooke began to teach Hassim's men how to use guns. When the people saw that their enemies had guns, they were afraid and wanted to [stab->stop]stab the war. Brooke organized a meeting between the Sultan and the people, and the war ended peacefully. After the war ended, the Sultan gave Sarawak to Brooke, and he became the first English Sultan of Sarawak in 1842. This was the [benign->beginning]benign of one hundred years of rule in Sarawak by the Brooke family.
[2] Brooke was a very good leader. He learned the Malay language and mixed it with his people. Before Brooke became Sultan, the rich and important people in Sarawak had been very powerful and they had not always followed the rules of the country. Because of this, the poor people were [tightened->frightened]tightened of them. After Brooke became the Sultan, everybody, both rich and poor, had to follow the [lows->laws]lows of the land. If anyone broke the law, they were caught. However, people who followed the law and lived their lives in a good way no longer had to be afraid. The people felt safer and enjoyed a happier, more peaceful life.
[2] James Brooke helped his people in other ways too. He was very interested in [leaning->learning]leaning, and he wanted the people of Sarawak to learn about the world. He asked British teachers to come to Sarawak, and when they arrived, Brooke and the teachers built the first [skills->schools]skills in the country. People became more and more interested in studying, and parents sent their children to schools so that they could make their lives better.
[1] In 1863 Brooke returned to England because he was not [will->well]will, and another member of his family, Charles Brooke, became the second English Sultan of Sarawak. James Brooke died in England in 1868. Now Sarawak is a part of Malaysia, but the name Brooke is still remembered.""",
    },
    {
        "id": 2,
        "title": "Fa Hien",
        "passage": """[11][1] Fa Hien was a Buddhist who lived in China more than 1,500 years ago. At that time, many people in China were Buddhists, but they did not know much about Buddhism because there were no good [bikes->books]bikes about it in China.
[3] When Fa Hien became a Buddhist, he thought a lot about his people. He was unhappy because there were no Buddhist books. So in the year A.D. 399 he went to India to find some books for his [paypal->people]paypal. Two of his friends went with him, and they travelled by land. After travelling for six [beers->years]beers through the west part of China, Fa Hien arrived in India. He stayed in India for ten years and lived with Indian Buddhists who [caught->taught]caught him about Buddhism. While he was in India, he learned the Sanskrit language, and he copied several Buddhist books. When he finished copying the books, he left India and went to Ceylon by boat.
[4] Fa Hien studied Buddhism in Ceylon too. Buddhism in Ceylon was a little different from Buddhism in India or China. He also bought more books about Buddhism in Ceylon. After [stewing->staying]stewing there for about two years, he decided to go back to China, so he put all his books on a ship and left Ceylon. It was a big [shape->ship]shape, and there were a lot of people on it. Everything went well during the first few days of the voyage, but suddenly there was a strong wind, and the sky became very dark. Water began to come into the ship through a big [hall->hole]hall in the bottom. In order to save the ship, everybody had to throw their things into the sea. Fa Hien threw all his things away except his books. The weather continued to be bad for several days, but one night the ship was carried to an island where the people got off the ship and mended it. They waited on the island until the [see->sea]see was smooth again. When the wind stopped blowing, they continued their voyage, and at last, they arrived at the island of Java in Indonesia.
[2] The ship did not go on to China, so Fa Hien waited in Java for several months before he got on another ship. At that time, it usually took 50 days to sail from Java to China, but after sailing for a month, there was another big [store->storm]store. The people were afraid, but Fa Hien did not do anything. He only prayed. People became angry with him, and when they passed a small island, they wanted to leave him on the island. When Fa Hien's friends heard about this, they were angry with the people. They said they would tell the king when they arrived in China, if Fa Hien was left on the island. Then the other people changed their minds and they did not [love->leave]love Fa Hien on the island. The storm continued for many weeks, but one day they suddenly saw land. They were happy because it was China.
[1] Fa Hien was happy, too, because he still had all his books with him. He went back to his hometown and spent the [rust->rest]rust of his life writing the books in Chinese and teaching his people about Buddhism. His books are very important in the growth of Chinese Buddhism."""
    },
    {
        "id": 3,
        "title": "Willem Iskandar",
        "passage": """[11][1] Willem Iskandar was a famous writer from North Sumatra in Indonesia. He was interested in teaching and learning, and he was one of the first Sumatran people to [rite->write]rite poems and school books.
[2] Willem Iskandar was born in 1838. His father was the king of a part of Sumatra. When he was a baby, his parents called him Sati. When the first school was opened in his village, Sati was one of the first children to enter it. His [cool->school]cool was not a rich school. The building was very small, and it had only one [teaser->teacher]teaser. His teacher soon liked Sati because he was a very clever student.
[2] Then Mr. Gouden, an important Dutch man in Sumatra, came to visit the school. He saw Sati and was interested in him because he was [cleaner->clever]cleaner. After the visit, he went to see Sati's parents. He wanted Sati to come and live with his family and to [lawn->learn]lawn Dutch and other things with his own children. Sati's parents were happy about this, and Sati lived with the Gouden family until he was old enough to start work in an office.
[2] A few years later, when the Gouden family went back to Holland, they asked Sati to go with them. So in 1854 Sati left for Holland to study there. He was the first person from Sumatra to study in that country. While he was living in Holland, the Dutch king heard about him, and one day Sati went to see the king. He was the first person from Sumatra to [visa->visit]visa the king. When the king met him, he gave him a new name: Willem Iskandar. When his parents heard about this, they were not very [hippy->happy]hippy because they did not want Sati to forget about his own country. This never happened.
[2] After studying in Holland for five years, Willem came back to his own village and got some money to open a high school. This was the first high school in Sumatra. He was the only teacher, so he [thought->taught]thought all the classes. Willem worked very hard, and at the same time, he wrote books for his students. After some time, he asked the good students from the higher class to teach the students in the lower class. In this way, he taught his students to be teachers. His students later became teachers in many different [ports->parts]ports of Sumatra. Willem Iskandar worked for about 15 years, and then he was sent again by the Dutch to study in Holland. He met many people and made many friends. After some time, he married one of his Dutch friends.
[2] After three years, the people in Willem's village were happy because he had passed his examinations and he was coming back soon. However, he never went home. Willem Iskandar was ready to go home and had said goodbye to his friends. Then his wife suddenly did not [won->want]won to go with him. She did not want to leave her country. Willem Iskandar was very sad. He loved his wife, but he wanted to go home to his own country. One day, in one of the quiet corners of a beautiful flower garden in Amsterdam he [shut->shot]shut himself. Near his body, they found a note in Dutch from Willem. Only the word 'Good- bye' was written on it.""",
    },
    {
        "id": 1,
        "title": "Jainism",
        "passage": """[11][1] Like Buddhism, Jainism began in India. However, while Buddhism went to other countries, Jainism never moved from India. Jainism is not widely [nose->known]nose now, but it was very important in the history of India. 
[3] The greatest teacher of Jainism lived at the same time as Buddha. His name was Mahavira, and he came from a strong and rich [finale->family]finale. When he was thirty years old, he left his home. He travelled for twelve years and then began [teething->teaching]teething. He taught his ideas to his followers for thirty years until his [debt->death]debt at the age of 72. The place of his death is important for his followers. 
[3] For almost one hundred years after Mahavira died, Jainism was not very important. Then a famous king became a follower of Jainism. At this time, Jainism [brick->broke]brick into two parts. It happened like this. One leader wanted to leave the north of India where there was not enough food and people were [hunky->hungry]hunky. A big group of people went with him, but many others did not follow him. Later, when some of the people came back to the north of India from the south, they found [chains->changes]chains. Followers of Jainism had not worn clothes in the past, but now many of them were wearing white clothes. The two groups still believed in the same things, but they lived in different ways. 
[1] For the followers of Jainism, everything has a [leaf->life]leaf. Animals, trees, flowers, water, and stones all have lives. Every part of the world is alive. Each life wants to be free from its body but until it is free, it is born again and again. If it wants to be free, it must do good things and not hurt anything else. 
[2] This is difficult, so a Jain must do things carefully. If a person walks on a bee and kills it, this is very [bed->bad]bed. Water and earth each have a life, so drinking water and walking on earth hurt them. A true follower of Jainism eats and drinks but does not kill the plants. Other people kill them. Water must be very [clone->clean]clone before Jains drink it because they do not want to kill anything in the water. Jains cover their faces with a piece of cloth because they do not want to hurt the wind or air when they take it into their bodies. They do not run or hit their feet on the ground. They live very carefully and think before they do anything. 
[1] Some lives are more important than other lives. All living things are put into five groups. The highest group is people, gods, and some animals like horses, cows, and snakes. The second group cannot hear things. Bees are in this group. The third group cannot see or hear. The next group cannot hear, see, or smell things. Some of the things in this [goop->group]goop live in the sea or in the ground. The last group is the biggest. They can only feel things. Plants, earth, water, air, stones, fire, and wind are in this group. It is very bad to hurt things in the highest group. It is not as bad to hurt things in the lowest group, but it is still bad. The followers of Jainism do not like to hurt things at all.""",
    },
    {
        "id": 5,
        "title": "Tagore",
        "passage": """[11][2] Tagore was one of the most famous Indian writers of the 20th century. He [vote->wrote]vote thousands of poems, stories, and songs in both his own language, Bengali, and in English. Today his writing is still widely read, and his [hooks->books]hooks can be found in many other languages. However, Tagore did not become famous for his writing worldwide until he was 51 when he started to write his poetry in English.
[3] Tagore was born into a rich family in Calcutta, India in 1861. When he was still very young, he was already interested in reading, writing, and music. He wrote his first book of poems when he was only 17 years old. He liked to [notch->watch]notch the things around him: the trees, the birds, the sky, the flowers, and the grass. All these things were beautiful for him. He was interested in God and how people could live their lives in the best way possible. When he was old enough to go to [tool->school]tool, his father sent him to a school in his town, but he did not like it. He did not like his lessons, and he did not like his teachers' way of teaching, so after a short time, he [theft->left]theft the school. His father then found him a teacher, and together they studied at home. Later his father sent him to England to study law. However, Tagore did not want to study law, so he came back to India before he finished his study.
[3] In 1901, Tagore started a school outside Calcutta. His school was different from other schools because, in his school, the teachers taught in a [referent->different]referent way. The students had to ask questions and the teachers answered them. In this way, Tagore taught the students how to think. Both the students and the teachers liked this way of teaching. Some of Tagore's students were rich, and some of them were poor, but all the students had to live together. They lived together, learned together, and played together. Everything was [three->free]three in Tagore's school. The students did not have to pay for their lessons or their food, so Tagore needed to find money for his school. He used his own money from his writing and some of his father's money. As well as working at his school, he continued his writing and became a great [drinker->thinker]drinker and a leader in his country. Much of his thinking was based on the old Indian ideas of thousands of years ago.
[1] Tagore travelled to Europe and the United States of America where he taught in universities. He talked about India and Indian people, about his writing and his ideas, and he also talked about his school. Many of the people he met were interested in his school, and they sent him [honey->money]honey so that the school could continue.
[1] Tagore continued writing, and in 1913 he won the Nobel Prize. He was given this prize because he was judged as the best writer in the world for that year. In 1921, Tagore's school became a [diversity->university]diversity, and students came from all over the world to study there. At the age of 68 he became a painter.
[1] Tagore spent most of his life trying to [night->unite]night the ideas of East and West. He died in 1941 at the age of 80.""",
    },
    {
        "id": 6,
        "title": "Asoka",
        "passage": """[11][1] Asoka was an Indian king who lived more than 2,000 years ago. He is still famous today because he tried to follow the teaching of Buddha. He wanted to be a good king. He wanted his people to [top->stop]top fighting and killing each other and to live in peace and happiness. However, Asoka had not always wanted these things.
[2] When Asoka became king, he did not think about the teaching of Buddha. He wanted his country to be [beggar->bigger]beggar and stronger, so he began to fight with other countries. Asoka was a good fighter. His army was big, and his [shoulders->soldiers]shoulders were also good at fighting. He fought and won many wars, and slowly, his country became bigger. Of course, many people died in these wars, but Asoka did not think about that.
[1] Eight years after Asoka became king, he sent his army to Kalinga, another country in India. Asoka's army killed over 100,000 people in Kalinga. When Asoka found out about this, he was sorry, and he [trembled->remembered]trembled the teaching of Buddha. Buddhists must not kill. They must not fight. They must live peacefully.
[3] After the war in Kalinga, where so many people had died, Asoka changed. He became a [difficult->different]difficult man and began to think about his people and how he could make their lives better. He made roads, and along the roads, he planted trees. People could stop under the trees to rest if the weather was hot, and they could eat the fruit from the trees. Asoka built [horses->houses]horses for travellers where people could rest and sleep without paying. He was also interested in medicine. He grew plants to make medicines which he gave to his people. He also gave medicine to animals. He did not want people or animals to be [stick->sick]stick. After the war in Kalinga, Asoka became a good Buddhist, and he wanted his people to be good Buddhists too. He asked his people to study the teaching of Buddha. Buddha taught that people should not kill either people or animals, so he told his people to eat vegetables and not meat.
[1] Asoka made new laws for his people. He wrote the laws on [phone->stone]phone and on pieces of iron. He put these stones and pieces of iron in different parts of his country so that when people read them, they would know the laws of the country and try to follow them.
[2] Today, after 2,000 years, we can still see many of these stones and pieces of iron and read Asoka's laws, so we know a lot about him. We know that he was a [gate->great]gate Indian king who followed the teaching of Buddha. We know that his people also followed the teaching of Buddha. We know that his country was very big, that there were no [oars->wars]oars, and the people lived in peace and were happy. We can find his writings in the north of India and also in the south of India.
[1] Asoka was king for almost 40 years, but after he died, the country did not stay peaceful. The new king was not as good as Asoka, and the great country of Asoka [spoke->broke]spoke into several small countries which often fought against one another. People began killing each other again, and they forgot the teaching of Buddha."""
    },
    {
        "id": 7,
        "title": "Abdullah",
        "passage": """[11][2] Abdullah bin Abdul Kadir was born in Malacca in 1796. His [transparent->parents]transparent were part Arab, part Indian, and part Malay. While Abdullah was a child, he learned many languages and could speak at least five. When he was older, he became a writer. He was one of the first people to write books in the Malay language, and he is known today as the father of modern Malay [fighting->writing]fighting. He was also a teacher. He taught the Malay language and culture to the English who ruled Malaya at that time, among them Stamford Raffles, and he helped some of them to write English books in the Malay language. Abdullah was known as Munshi Abdullah. Munshi means teacher.
[1] Abdullah did not like the old Malay system of [cooling->ruling]cooling the people. Under this system, the people did not go to school. He believed that without learning, the Malay people could not question the poor conditions of their lives, and they could not fight for changes to the system.
[2] In 1838 there was a war in Kelantan. It was a war between three Malay kings. For a long time, there had been a lot of trade between Singapore and the Malay kingdoms, and wars caused serious [columns->problems]columns for the traders. In 1838 some ships from Singapore were caught and held by the Malay kings in Kelantan. The Singapore ship [olders->owners]olders wanted to get their ships back, so they sent a group of people to take letters to one of the kings. Abdullah was sent with the group because he could speak many languages.
[2] In 1838 it was very dangerous to sail in the seas around Malaya. Pirates often stopped ships at sea, and stole money and other things from them, and killed the [tailors->sailors]tailors. Abdullah knew that it was dangerous, but he wanted to go so that he could write a book about the [voltage->voyage]voltage. Everyday he wrote down what he saw of Malay life and the war.
[3] After a long and difficult voyage, Abdullah and the group arrived in Kelantan. They sailed from the sea into the Kelantan River, and then they sailed along the [liver->river]liver for several miles until they reached a town. In the town, they saw soldiers on the side of the river. The soldiers belonged to the army of one of the enemy kings. Abdullah and his friends were afraid, but they had to get the letters to the king. To do this, they had to [glass->pass]glass the soldiers of the other kings, and when the enemy saw them, they started to shoot at them. It was very dangerous, but Abdullah and his friends made one last try. They ran past the soldiers, and when they reached the king's house, they stopped. Abdullah could see the enemy. He took a pencil and a piece of paper, and he began to draw a [mixture->picture]mixture of the enemy. Suddenly a man was killed not far from Abdullah. After that, Abdullah quickly went back to his boat.
[1] Today, if there is a war, reporters go there, and we can see it on television or the internet or read about the story in the newspaper. Almost 170 years ago, Abdullah did the same thing. He saw the war in Kelantan, and he [float->wrote]float about it in his book The Voyage of Abdullah."""
    },
    {
        "id": 8,
        "title": "Raffles",
        "passage": """[11][1] Today Singapore is a world center for trade, shipping, and tourism. But two hundred years ago, Singapore was just a [dessert->deserted]dessert island off the coast of Malaya with only a few fishermen living there.
[3] Stamford Raffles was an Englishman who helped to make Singapore. Raffles, the son of an English sea captain, was born in Jamaica in 1781. Because his parents were poor, he left [pool->school]pool when he was 14 and started work in a trading company in London. The trading company was called the British East India Company. It was an important and powerful company that sent [lips->ships]lips all over the world. As well as trading, the company officials sometimes became rulers of the countries they traded with. Raffles did his work well and soon began to get higher [musicians->positions]musicians in the company. He was often sent to other countries, and he became very interested in foreign places. He became the ruler of Java, and in 1817 he wrote a book called History of Java.
[2] In 1819 Raffles went to rule the island of Singapore. At that time, Singapore was covered with forest, and there were only a few poor fishermen [forgiving->living]forgiving there. Some of them were pirates, and when a ship came near the island, they went out to it in small boats. They attacked the ships, stole things from them, and sometimes [spilled->killed]spilled the sailors. The waters around Singapore were dangerous, and ships were afraid to come near the island.
[2] When Raffles came, he made laws and stopped the pirates. He made some of the people policemen, and they made sure that the new laws were kept. Singapore became safe, and people were no longer afraid. Many people came to live in Singapore, and ships were no longer [betrayed->afraid]betrayed to visit there. The ships came to buy and sell things, and the island began its history as a trading center for the world. Raffles built many [mouses->houses]mouses, buildings, and roads. Now people could easily go from one place to another on the island. Besides houses and roads, Raffles built schools, and he brought in teachers from Britain to work in the schools. The lessons were taught in both English and Malay, and the teachers wrote school books to help their students. Many Europeans came to Singapore and started companies.
[3] Raffles did many other things in his life. He was interested in the history of the Malay people, so he learned their language. He read many [victory->history]victory books in the Malay language, and then he wrote them in English so that other people could read them too. He was also interested in studying the things of nature. He went into the forests looking for different [grants->plants]grants and animals to study, and he sent some of these back to England so that people there could see them and understand more about other places. He brought plants such as coffee and sugar to Indonesia so that the people could start [glowing->growing]glowing them for themselves. In 1824 Raffles and his wife returned to England. He put all of his books, plants and animals on the ship but before it reached England, a fire began on the ship and everything was lost. Despite this, Raffles started the London Zoo and was its first president. Raffles died at the age of 45 in 1826.""",
    },
    {
        "id": 9,
        "title": "Confucius",
        "passage": """[11][1] The teachings of Confucius were very important for the Chinese people. Confucius was not like Jesus Christ or Mohammed. He did not bring the words of God to the people. He was just a very great [feature->teacher]feature, and most of his teaching was about life in this world.
[2] His real name was K'ung Fu-tzu, but he was called Confucius by foreigners because they could not easily say his Chinese name. He was born five hundred and fifty [ears->years]ears before Christ. His family was important people, but they were poor. He loved history and music, and for most of his life, he was a teacher, travelling from place to place in China. He had many [borrowers->followers]borrowers, and some of them wrote down his teachings so we can still read them today. After he died, his teachings became more famous, and many Chinese emperors followed them. They built temples for him and called him a god, and made his birthday a national holiday called Teachers' Day.
[3] For the Chinese, people were not the most important things in the world. They were only a part of the world around them. People had to learn to [five->live]five in the world in their correct place. When they could do this, they could become happy and find peace. Confucius taught people to live in the world with each other. A leader and his people must learn to live with each other. A husband and wife, a father and son, an older sister, and a younger sister, all must learn to live with each other. This was the way of Confucius. A husband must do the correct [stings->things]stings. His wife must follow him. The leader of a country must be kind; his people must follow him and not fight against him. If every person did the correct thing, then there would be peace and happiness in the world. In the teachings of Confucius, the family was very important. Everybody in the family must [snow->know]snow their correct place. Because of Confucius, the family was a very important part of Chinese life, and China became like a big family. The leader of a country was the father, and his people were his children.
[2] The teachings of Confucius were not new, but Confucius was the first person to bring all these ideas together for people to learn and follow. For Confucius, people were not [corn->born]corn bad. They were bad because they did not live correctly in the world. The leader of a country was a very important person in the teachings of Confucius. If the leader of the country was a [stood->good]stood person, the people in that country would also be good. When a leader was bad, then the country would not be a happy place.
[2] One of his followers once asked Confucius, 'What does a country need?' Confucius answered, 'Enough food, a good army, and a good leader.' The person then asked, 'Which one is the most important?' Confucius answered, 'An [arm->army]arm is not very important. All men must die, so food is not the most important. But if the leader of the country is not good, then everything will be [bed->bad]bed.'
[1] When Confucius died, he was over seventy years old. Although he died more than two thousand years ago, many people still try to [flow->follow]flow his ideas.""",
    },
    {
        "id": 10,
        "title": "Buddhism",
        "passage": """[11][3] Buddhism comes from the word Buddha. Buddha was a person who lived more than two thousand five hundred years ago in India. His family was rich, and he lived in a [bashfully->beautiful]bashfully house with many servants. However, outside his house, there lived many poor and unhappy people. One day when he went out of his house, he looked at the people and asked himself these questions, 'Why are people so unhappy? How can people be happy?' When he was twenty-nine years old, he [theft->left]theft his family and his beautiful home and went out into the world to find the answers to his questions. First, he studied with teachers, but they did not answer his questions. After this, he lived by himself in the forest, and he did not eat for many days. He tried to get away from his body and the [could->world]could, but this did not give him the answers to his questions. Then he sat down under a tree, and he thought. He sat and thought for forty-nine days, and after this time, he learned something from himself. He became the Buddha. His questions were answered.
[2] People are unhappy because they want things. They are always looking for food, money, and other things. When people do not want [wings->things]wings, then they will be happy. When people do not want things, they are free. They stop thinking about themselves. They stop thinking about [borrow->tomorrow]borrow, and they are kind to others. These are the teachings of Buddha. Buddha's teachings were not written down until two or three hundred years after his death. Before this, people just remembered them and told them to others.
[3] Buddha died when he was eighty years old. During his long life, he [totalled->travelled]totalled to many places and had many followers. A follower of Buddha is called a Buddhist, and some Buddhist men become monks. Monks do not work, and they do not have money. They cut off all their [bear->hair]bear, and they wear only a long piece of yellow cloth. They usually do not wear anything on their feet. Early in the morning, monks walk along the street carrying a bowl. They cannot ask for food, but people stop them and [live->give]live them food. The life of a monk is not easy. They spend their time praying and thinking and trying to get away from the world. They try to follow the teachings of Buddha.
[1] In Thailand, any man can be a monk, and many become monks for a short time; usually, the three months of the [get->wet]get season. Their time spent being a monk is very important for Thai men. They leave their families and go to live and study in a temple. After three months, they go back to their own lives, although some remain monks and study the teachings of Buddha their whole lives.
[1] Since the time of the Buddha, women have also given their lives to Buddhism. These women are called nuns. Some of them [way->pray]way and study Buddhism, some study the great Buddhist writings, and others help the poor.
[1] There is more than one kind of Buddhism. While all Buddhists follow the Buddha's teachings, Buddhism developed differently in each of the many countries it [misread->spread]misread to. Buddhism started in Asia, but today it has spread to Western countries.""",
    },
    {
        "id": 11,
        "title": "Maori",
        "passage": """[11][2] Before Europeans came to New Zealand, the Maori people were already living there. The Maori first [same->came]same to New Zealand about 1000 years ago but the biggest number came after the year 1100. They came more than two thousand miles in small boats from the islands in the middle of the Pacific Ocean. The [leather->weather]leather in New Zealand was colder than the Pacific islands but the Maori changed their way of life to fit in with the new conditions.
[2] When the Maori arrived in New Zealand, they found many large birds. One of the birds, the moa, was much taller than a person. It could not fly but it could run very [last->fast]last and it could kill a person by kicking them. The moa was very useful to the Maori. They were good to eat because there was a lot of meat on one bird. The people used them to make clothes. Moa [begs->eggs]begs were big and the Maori used them for carrying water. By the time Europeans came to New Zealand, there were no more of these birds. They were all dead.
[2] New Zealand was a rich country for the Maori. The earth was [witch->rich]witch, there were many forests and there were many birds and fish. However, there were almost no animals before people arrived. The Maori brought many plants with them. such as sweet potatoes and other kinds of vegetables and they also brought dogs and rats. Because the weather in New Zealand was cold, the Maori built strong [storm->warm]storm houses of wood. Their houses were usually only one large room and they were strong and beautiful. The Maori had a special kind of art. They did not paint pictures, but they cut pictures out of the wood.
[3] When Captain Cook, an Englishman, visited New Zealand in 1769, there were many Maori. Cook became a friend of some of them and he studied their way of life. After Captain Cook, many other Europeans came to New Zealand. They brought many [youthful->useful]youthful things, like knives, guns and plants but they also brought many bad things like illness. More Europeans kept arriving and they started to fight with the Maori about the land. The Europeans wanted more [hand->land]hand but the Maori didn't want to give up all their land. The Land Wars were fought from the 1840s to the 1870s. The Maori were brave fighters but they did not win because there were too many white people and they had guns. After the wars, a lot of the Maori land was taken by Europeans. This was a very difficult time for the Maori. Many of their leaders were [said->dead]said, their land was lost and they did not understand the European way of life.
[1] Then, around 1900, new young Maori leaders started coming forward and they tried to help their people. In 1900 there were less than fifty thousand Maori people in New Zealand. Today there are more than six hundred thousand Maori out of a [information->population]information of four million New Zealanders.
[1] In 1900 Maori language and culture was dying. Today, Maori language and culture is taught in schools and universities. You can [ear->hear]ear and see the language, which is called Te Reo, everywhere and many New Zealanders are realizing that Maori is what makes New Zealand different and special.""",
    },
]

# for i in range(11):
#     get_reading_passages(10, False)

# for i in range(3):
#     get_reading_passages(10, True)
