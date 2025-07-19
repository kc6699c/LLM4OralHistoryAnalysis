# Semantic Classification Prompt

## Foundational Prompt

### Instruction

You're working on a project about the history of Japanese incarceration. You have enough knowledge about this domain and can consider the contexts inside the category. Classify transcripts in each row into the corresponding topic category.
The sentences are from the Densho repository, an extensive digital archive focused on the history of Japanese Americans during World War II.
The repository aims to preserve and share the stories of Japanese Americans who were forcibly relocated and incarcerated in internment camps by the U.S. government following the attack on Pearl Harbor. Return only the category number as outputs.

### Categories:
0 - Biographic Information of the person 
1 - Life Before Removal
2 - Life during the Incarceration 
3 - Military services 
4 - Returning of Japanese Americans after WWII 
5 - Movements for peace and justice

## Structured Prompt
### Instruction
You're working on a project about the history of Japanese incarceration. You have enough knowledge about this domain and can consider the contexts inside the topic.
Based on your memory and the below definitions for each topic, classify transcripts in each row into the corresponding topic category.
The sentences are from the Densho repository, an extensive digital archive focused on the history of Japanese Americans during World War II.
The repository aims to preserve and share the stories of Japanese Americans who were forcibly relocated and incarcerated in internment camps by the U.S. government following the attack on Pearl Harbor. Return only the topic numbers as outputs. Return only the topic category number as outputs. 

### Topic Categories
0 - Biographic Information of the person
1 - Life Before Removal
2 - Life during the Incarceration 
3 - Military services 
4 - Returning of Japanese Americans after WWII
5 - Movements for peace and justice 

### Definitions
#### Category 0: Biographic Information
This category includes sentences that can be considered as self-introductions, excluding names. Information about the narrators themselves, including birth stories, families (only their birthdays and stories about how they came to the U.S.), and places where they lived, are categorized here. Detailed explanations about communities go to Category 1. Some people were born in camps; such sentences should be labeled under Category 1, not Category 2.

#### Category 1: Life Before Removal
This category includes stories such as how they or their (grand)parents came to the U.S. from Japan, their cultural life, jobs, school life, and relationships with neighbors and friends. Keywords include a story to come to the U.S., neighborhood, friend, job, school, community, and discrimination.

#### Category 2: Life During the Incarceration
This topic includes stories about the day Japan attacked Pearl Harbor, interactions with the FBI, being sent to internment camps and life in the camps. The key sentence could be, “Can you tell us a bit about your memories of Pearl Harbor, December 7, 1941?” Keywords are: the day Japan attacked, the day the U.S. government announced the incarceration order, camp conditions, job, school, hobby, injustice, and discrimination. 

#### Category 3: Military Services 
This category includes stories about the military achievements of Japanese Americans, drafts for the American or Japanese Army, the loyalty questionnaire for the army draft conducted in the camps, and any other relevant stories.

#### Category 4: Returning of Japanese Americans After WWII 
In this category, the key sentence is, “After you left the camp….” This includes stories about whether they were able to find jobs, difficulties in getting hired even as veterans, continued discrimination due to the Japanese attack, and where they worked (if it’s ‘JACL’, then label it Category 5). Key components include life after incarceration, job, and discrimination.

#### Category 5: Movements for Peace and Justice
This category includes reflective thoughts on the redress and reparations movement for Japanese Americans, the perceived delays and impacts of these efforts, and broader societal lessons or lack thereof from the internment experience. It covers their thoughts on war or peace and participation in movements like the redress movement. Key components include movement, JACL, peace, and justice."



## Comprehensive Prompt
### Instruction 
You're working on a project about the history of Japanese incarceration. You have enough knowledge about this domain and can consider the contexts inside the category.
Based on your memory, the definitions for each category, and the background information of Japanese Americans and their incarceration history below, classify transcripts in each row into the corresponding to the category. 
The sentences are from the Densho repository, an extensive digital archive focused on the history of Japanese Americans during World War II.
The repository aims to preserve and share the stories of Japanese Americans who were forcibly relocated and incarcerated in internment camps by the U.S. government following the attack on Pearl Harbor. Return only the category number as outputs.

### Topic Categories
0 - Biographic Information of the person
1 - Life Before Removal
2 - Life during the Incarceration 
3 - Military services 
4 - Returning of Japanese Americans after WWII
5 - Movements for peace and justice 

#### Category 0: Biographical Information
Sentences in this category should focus on factual details about individuals, such as their name, birthdate, birthplace (including camps), family members, or religious affiliations. It also includes sentences mainly describing how old they were when they came to the U.S. (e.g., “My father came to the U.S. in 1905 at the age of fifteen with his father”) without a broader context about their lives or experiences in the new country, then they must be labeled here, otherwise in Category 1. If the sentence provides additional context about their life in the U.S., such as challenges, achievements, community involvement, family life, or education, it should be categorized in Category 1 instead. For example, sentences about establishing a business, adapting to a new culture, or interacting with the community belong in Category 1, even if they also include factual details.

#### Category 1: Life Before Removal
This category includes sentences that describe how Japanese Americans or their families lived before the declaration of incarceration. It encompasses their daily lives, educational experiences, cultural practices, community dynamics, and the challenges they faced, such as racial discrimination or political tensions leading up to World War II. It also includes sentences about family customs, cultural teachings, and social hierarchies passed down within families, including Japanese traditions, values, and practices instilled by parents or elders. For example, reflections on how children were taught to follow Japanese customs, or observe traditional roles in the family fit into this category. Sentences that reflect societal attitudes, media portrayals, or policies (e.g., Alien Registration Act) before Pearl Harbor or the declaration of incarceration also belong here. If sentences primarily focus on factual details (e.g., names, birthdates, birthplaces, or religious affiliations) without additional life context, they should be categorized in Category 0 instead.
Sentences also can be about the story of how they came to the U.S. but if they include factual biographical information (e.g., “My father was 19 when he came to the U.S.”) without a broader life context, it should be categorized in Category 0 instead.
While sentences about pre-war discrimination, anti-Japanese sentiment, or the political environment may refer to the growing threat of war, they are still part of the pre-incarceration context and should remain in this category. Additionally, personal reflections on how societal attitudes evolved leading up to the war, or the ways these attitudes shaped Japanese Americans' lives, should be categorized here.
If sentences discuss specific events or societal struggles after Pearl Harbor or during the incarceration period, such as transportation to camps, FBI investigations, or experiences within the camps, they should be categorized in Category 2.

#### Category 2: Life During the Incarceration
This category includes sentences describing events and experiences spanning from the day Japan bombed Pearl Harbor (December 7, 1941) to the end of incarceration, encompassing the period leading up to internment. It captures societal struggles, acts of discrimination, and preparations for removal, as well as the daily realities of life in incarceration camps. Stories in this category may include memories of Pearl Harbor and the immediate societal fallout, such as FBI investigations, heightened community tensions, and both acts of kindness and hostility. They also cover personal challenges during the removal process, including packing belongings, selling off property, and bidding farewell to friends and neighbors, as well as experiences during transportation to camps or while awaiting relocation orders, often marked by discrimination and difficulties accessing services. Additionally, this category encompasses life within the camps, including food, work, education, recreation, and the social dynamics of those confined together.
This category also includes legal challenges or defiance of laws during the incarceration period, such as acts of civil disobedience or challenges to curfews, incarceration orders, or other wartime restrictions. Narratives reflecting on these events as they occurred during the incarceration time, whether supportive or critical, also belong here. Furthermore, perspectives from non-Japanese individuals about the removal or treatment of Japanese Americans during this time fit within this category.
Category 2 focuses on events tied directly to incarceration and wartime struggles. If sentences focus primarily on pre-war life, such as stories about businesses, schools, neighborhood life, societal attitudes, or challenges leading up to Pearl Harbor and incarceration, they should be categorized in Category 1 instead.

#### Category 3: Military Services
This category includes sentences that describe decisions about military service, whether individuals chose to join the U.S. Army, resisted conscription, or, in some cases, considered service in the Japanese Army. It also encompasses reflections on the loyalty questionnaire, particularly questions related to allegiance to the U.S. and military service, along with the consequences of their responses. Sentences in this category often explore societal perceptions and judgments of those who served, resisted, or expressed defiance, including terms like "yes-yes" or "no-no" and their broader implications.
Additionally, this category includes sentences discussing the post-war benefits and opportunities that stemmed from military service, such as gaining employment, accessing education, or receiving recognition through veterans' programs. If a sentence primarily focuses on military service, the loyalty questionnaire, or the societal and personal impacts of military involvement, it should be categorized here rather than in Category 2. 

#### Category 4: Returning of Japanese Americans after WWII
This category must include sentences describing stories after the war ended, focusing on adjustments to life after leaving the camps or surviving in post-war Japan. These stories may consist of challenges like finding employment, gaining access to education, and dealing with societal treatment in the U.S. or Japan. Narratives about the survival strategies of those in Japan, such as participating in illegal markets or navigating post-war chaos, also fall under this category, as do interactions with American soldiers or the impact of post-war policies on civilians. Additionally, this category includes reflections on the emotional and societal aftermath of the war, such as shock at Japan's surrender, the chaos of rebuilding lives, and how people coped with these changes. Narratives by non-Japanese individuals about their perspectives on welcoming or rejecting Japanese Americans also belong here. 

#### Category 5: Movements for peace and justice
This category includes sentences describing redress movements and other activities aimed at seeking justice after the war ended. It focuses on efforts to address the wrongs of incarceration, how individuals and communities advocated for recognition, reparations, or historical acknowledgment, and reflections on the broader lessons learned from the incarceration experience. Sentences reflecting on the impact of these movements or the legacy of the incarceration history during interviews also belong here.
Legal challenges or acts of resistance occurring during the incarceration period, such as defying curfews or incarceration orders, belong in Category 2 unless they are explicitly discussed in the context of post-war justice movements.


### Background of Japanese American Incarceration
The history of Japanese Americans began with the arrival of the Issei, or “first generation,” who came to the United States as early as 1869. This initial group included laborers who worked in Hawaii’s sugarcane fields and California’s farms. By the early 20th century, Japanese immigration had significantly increased, with the 1900 U.S. Census recording 24,326 Japanese residents in America, mostly men. Despite restrictive measures like the 1907 Gentlemen’s Agreement and the 1913 California Alien Land Law, designed to limit Japanese immigration and prevent land ownership, the community continued to grow. The 1924 Immigration Act further restricted Japanese immigration until 1952, but by then, Japanese Americans had established vibrant communities. They developed businesses, religious institutions, and successful agricultural enterprises, particularly in the San Joaquin Valley. Kenjinkai, regional affinity clubs, offered mutual support and fostered community connections, while the Japanese American Citizens League (JACL), formed around 1930, played a crucial role in civil rights and addressing tensions between Issei and U.S.-born Japanese Americans. Both organizations have been vital in preserving Japanese American culture and advocating for their rights. During this time, on December 7th, 1941, one big news came out that the Japanese Army attacked Pearl Harbor. This unexpected assault not only marked America's entry into World War II but also triggered a wave of suspicion and hostility towards Japanese Americans. In the immediate aftermath, Japanese Americans faced severe repercussions. In Hawaii, where many of the casualties were Japanese American civilians, authorities swiftly detained community leaders and suspected individuals without formal charges. This led to widespread fear and disruption, with martial law imposed for nearly three years. On the mainland, the consequences were more gradual but no less intense. Within months of the attack, Executive Order 9066 was signed, leading to the mass removal and incarceration of Japanese Americans. The number of those affected is often cited as between 110,000 and 120,000, depending on the context. The 110,000 figure refers to those forcibly removed from the West Coast, while the 120,000 figure includes those held in camps at various times, including those transferred from other detention systems and new arrivals from Hawaii. Additionally, some estimates suggest that the true number of incarcerated Japanese Americans might be slightly higher when including those in assembly centers and other detention facilities not covered by the War Relocation Authority’s records.

### Key Words
0 - Biographical Information: Factual details about individuals (e.g., name, birthdate, birthplace, family, religion).
1 - Life Before Removal: Daily life, education, culture, life context, discrimination, or policies affecting Japanese Americans before WWII. Pre-war struggles belong here unless explicitly tied to incarceration.
2 - Life During Incarceration: Events from Pearl Harbor (Dec 7, 1941) to the end of internment—FBI investigations, forced removals, camp life, legal defiance, and wartime struggles. 
3 - Military Service: Decisions on U.S. or Japanese military service, the loyalty questionnaire, and post-war veteran experiences.
4 - Returning of Japanese Americans after WWII: Adjusting after WWII—finding jobs, education, discrimination, and post-war survival in the U.S. or Japan.
5 - Movements for peace and justice: Post-war redress efforts, legal challenges, and reflections on the incarceration legacy.




## Refined Prompt
You're working on a project about the history of Japanese incarceration. You have enough knowledge about this domain and can consider the contexts inside the topic.
Based on your memory and the below definitions for each topic, classify transcripts in each row into the corresponding topic category.
The sentences are from the Densho repository, an extensive digital archive focused on the history of Japanese Americans during World War II.
The repository aims to preserve and share the stories of Japanese Americans who were forcibly relocated and incarcerated in internment camps by the U.S. government following the attack on Pearl Harbor. Return only the topic numbers as outputs. Return only the topic category number as outputs. 

### Topic Categories
0 - Biographic Information of the person
1 - Life Before Removal
2 - Life during the Incarceration 
3 - Military services 
4 - Returning of Japanese Americans after WWII
5 - Movements for peace and justice 

#### Category 0: Biographical Information
Sentences in this category should focus on factual details about individuals, such as their name, birthdate, birthplace (including camps), family members, or religious affiliations. It also includes sentences mainly describing how old they were when they came to the U.S. (e.g., “My father came to the U.S. in 1905 at the age of fifteen with his father”) without a broader context about their lives or experiences in the new country, then they must be labeled here, otherwise in Category 1. If the sentence provides additional context about their life in the U.S., such as challenges, achievements, community involvement, family life, or education, it should be categorized in Category 1 instead. For example, sentences about establishing a business, adapting to a new culture, or interacting with the community belong in Category 1, even if they also include factual details.

#### Category 1: Life Before Removal
This category includes sentences that describe how Japanese Americans or their families lived before the declaration of incarceration. It encompasses their daily lives, educational experiences, cultural practices, community dynamics, and the challenges they faced, such as racial discrimination or political tensions leading up to World War II. It also includes sentences about family customs, cultural teachings, and social hierarchies passed down within families, including Japanese traditions, values, and practices instilled by parents or elders. For example, reflections on how children were taught to follow Japanese customs, or observe traditional roles in the family fit into this category. Sentences that reflect societal attitudes, media portrayals, or policies (e.g., Alien Registration Act) before Pearl Harbor or the declaration of incarceration also belong here. If sentences primarily focus on factual details (e.g., names, birthdates, birthplaces, or religious affiliations) without additional life context, they should be categorized in Category 0 instead.
Sentences also can be about the story of how they came to the U.S. but if they include factual biographical information (e.g., “My father was 19 when he came to the U.S.”) without a broader life context, it should be categorized in Category 0 instead.
While sentences about pre-war discrimination, anti-Japanese sentiment, or the political environment may refer to the growing threat of war, they are still part of the pre-incarceration context and should remain in this category. Additionally, personal reflections on how societal attitudes evolved leading up to the war, or the ways these attitudes shaped Japanese Americans' lives, should be categorized here.
If sentences discuss specific events or societal struggles after Pearl Harbor or during the incarceration period, such as transportation to camps, FBI investigations, or experiences within the camps, they should be categorized in Category 2.

#### Category 2: Life During the Incarceration 
This category includes sentences describing events and experiences spanning from the day Japan bombed Pearl Harbor (December 7, 1941) to the end of incarceration, encompassing the period leading up to internment. It captures societal struggles, acts of discrimination, and preparations for removal, as well as the daily realities of life in incarceration camps. Stories in this category may include memories of Pearl Harbor and the immediate societal fallout, such as FBI investigations, heightened community tensions, and both acts of kindness and hostility. They also cover personal challenges during the removal process, including packing belongings, selling off property, and bidding farewell to friends and neighbors, as well as experiences during transportation to camps or while awaiting relocation orders, often marked by discrimination and difficulties accessing services. Additionally, this category encompasses life within the camps, including food, work, education, recreation, and the social dynamics of those confined together.
This category also includes legal challenges or defiance of laws during the incarceration period, such as acts of civil disobedience or challenges to curfews, incarceration orders, or other wartime restrictions. Narratives reflecting on these events as they occurred during the incarceration time, whether supportive or critical, also belong here. Furthermore, perspectives from non-Japanese individuals about the removal or treatment of Japanese Americans during this time fit within this category.
Category 2 focuses on events tied directly to incarceration and wartime struggles. If sentences focus primarily on pre-war life, such as stories about businesses, schools, neighborhood life, societal attitudes, or challenges leading up to Pearl Harbor and incarceration, they should be categorized in Category 1 instead. 

#### Category 3: Military services 
This category includes sentences that describe decisions about military service, whether individuals chose to join the U.S. Army, resisted conscription, or, in some cases, considered service in the Japanese Army. It also encompasses reflections on the loyalty questionnaire, particularly questions related to allegiance to the U.S. and military service, along with the consequences of their responses. Sentences in this category often explore societal perceptions and judgments of those who served, resisted, or expressed defiance, including terms like ""yes-yes"" or ""no-no"" and their broader implications.
Additionally, this category includes sentences discussing the post-war benefits and opportunities that stemmed from military service, such as gaining employment, accessing education, or receiving recognition through veterans' programs. If a sentence primarily focuses on military service, the loyalty questionnaire, or the societal and personal impacts of military involvement, it should be categorized here rather than in Category 2.

#### Category 4: Returning of Japanese Americans after WWII 
This category must include sentences describing stories after the war ended, focusing on adjustments to life after leaving the camps or surviving in post-war Japan. These stories may consist of challenges like finding employment, gaining access to education, and dealing with societal treatment in the U.S. or Japan. Narratives about the survival strategies of those in Japan, such as participating in illegal markets or navigating post-war chaos, also fall under this category, as do interactions with American soldiers or the impact of post-war policies on civilians.
Additionally, this category includes reflections on the emotional and societal aftermath of the war, such as shock at Japan's surrender, the chaos of rebuilding lives, and how people coped with these changes. Narratives by non-Japanese individuals about their perspectives on welcoming or rejecting Japanese Americans also belong here. 

#### Category 5: Movements for Peace and Justice
This category includes sentences describing redress movements and other activities aimed at seeking justice after the war ended. It focuses on efforts to address the wrongs of incarceration, how individuals and communities advocated for recognition, reparations, or historical acknowledgment, and reflections on the broader lessons learned from the incarceration experience. Sentences reflecting on the impact of these movements or the legacy of the incarceration history during interviews also belong here.
Legal challenges or acts of resistance occurring during the incarceration period, such as defying curfews or incarceration orders, belong in Category 2 unless they are explicitly discussed in the context of post-war justice movements.

### Key Words
0 - Biographical Information: Factual details about individuals (e.g., name, birthdate, birthplace, family, religion).
1 - Life Before Removal: Daily life, education, culture, life context, discrimination, or policies affecting Japanese Americans before WWII. Pre-war struggles belong here unless explicitly tied to incarceration.
2 - Life During Incarceration: Events from Pearl Harbor (Dec 7, 1941) to the end of internment—FBI investigations, forced removals, camp life, legal defiance, and wartime struggles. 
3 - Military Service: Decisions on U.S. or Japanese military service, the loyalty questionnaire, and post-war veteran experiences.
4 - Returning of Japanese Americans after WWII: Adjusting after WWII—finding jobs, education, discrimination, and post-war survival in the U.S. or Japan.
5 - Movements for peace and justice: Post-war redress efforts, legal challenges, and reflections on the incarceration legacy.






## Concise Prompt
You're an expert in Japanese American incarceration history. Classify each transcript into one of the categories below based on its content. The sentences come from the Densho repository, which documents the forced relocation and internment of Japanese Americans during WWII. Return only the topic number. 

#### Category 0 – Biographical Information
Factual personal details: name, birthdate, birthplace (including camps), age of migration, religion, or family structure. No life story or social context.
Keywords: born, name, family, religion, siblings, birthplace, father came at age X.

#### Category 1 – Life Before Removal
Life in the U.S. before Pearl Harbor: daily life, schooling, work, discrimination, traditions, or immigration stories with context.
Keywords: Daily life, education, culture, life context, discrimination, or policies affecting Japanese Americans before WWII. Pre-war struggles belong here unless explicitly tied to incarceration, before the war, racism, school, farming, church, learning Japanese ways, community, Alien Registration Act.

#### Category 2 – Life During the Incarceration 
From Pearl Harbor to camp release: arrest, exclusion orders, relocation, camp life, curfews, FBI raids, camp jobs/schools.
Keywords: Pearl Harbor, sent to camp, evacuation, barracks, dust, curfew, mess hall, FBI, "assembly center".

#### Category 3 – Military Services
Military involvement: Events from Pearl Harbor (Dec 7, 1941) to the end of internment—FBI investigations, forced removals, camp life, legal defiance, and wartime struggles, volunteering, draft resistance, serving in U.S. or Japanese armies, loyalty questionnaire, 442nd, “no-no boys.”
Keywords: army, drafted, 442nd, loyalty, service, enlist, resist, question 27 and 28, Decisions on U.S. or Japanese military service, the loyalty questionnaire, and post-war veteran experiences.

#### Category 4 – Returning of Japanese Americans After WWII
Life after release: returning home, finding jobs, facing hostility, resettling in the U.S. or surviving post-war Japan.
Keywords: after the war, return home, job search, rebuild, GI Bill, Adjusting after WWII—finding jobs, education, discrimination, and post-war survival in the U.S. or Japan.

#### Category 5 – Movements for Peace and Justice
Post-war redress, advocacy, public recognition, reparations, and lessons from incarceration.
Keywords: redress, apology, reparations, activism, hearings, Commission, injustice, Civil Liberties Act, Post-war redress efforts, legal challenges, and reflections on the incarceration legacy.

Focus on content meaning rather than keywords. If unclear, classify based on the primary theme of the sentence.
