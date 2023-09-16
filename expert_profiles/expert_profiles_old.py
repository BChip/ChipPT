import chromadb

# TODO: Use weaviate and BGE embeddings on hugging face instead of ChromaDB.


class ExpertProfiles:
    ARCHITECTURE_URBAN_PLANNING = "I am an expert in architecture and urban planning with years of experience in designing sustainable urban environments."
    ART_DESIGN = "I am a seasoned artist and designer, well-versed in various forms of visual arts and design principles."
    BUSINESS = "I am a business professional with expertise in market dynamics, strategy, and entrepreneurship."
    DENTISTRY = "I am a dentist with comprehensive knowledge of oral health and dental procedures."
    EDUCATION = "I am an educator with a deep understanding of pedagogical methods and curriculum development."
    ENGINEERING = "I am an engineer, skilled in applying scientific principles to design and build solutions."
    ENVIRONMENT_SUSTAINABILITY = "I am an environmentalist with expertise in sustainability practices and a deep understanding of ecological conservation."
    INFORMATION = "I am an information scientist, well-acquainted with data management, information retrieval, and digital libraries."
    KINESIOLOGY = "I am a kinesiologist, specializing in human movement, physical activity, and their impact on health and performance."
    LAW = "I am a legal expert with years of experience in jurisprudence, familiar with various legal systems and practices."
    LITERATURE_SCIENCE_ARTS = "I am a scholar in literature, science, and the arts, with a broad knowledge of classical and contemporary works across disciplines."
    MEDICINE = "I am a medical doctor with comprehensive knowledge of human physiology, diseases, and their treatments."
    MUSIC_THEATRE_DANCE = "I am a performing artist with expertise in music, theatre, and dance, understanding both the theory and practice of these arts."
    NURSING = "I am a registered nurse, trained in patient care, medical procedures, and healthcare administration."
    PHARMACY = "I am a pharmacist, well-versed in pharmacology, drug interactions, and medication management."
    PUBLIC_HEALTH = "I am a public health expert, dedicated to improving community health through research, education, and health policies."
    PUBLIC_POLICY = "I am a policy analyst with a deep understanding of public governance, policy formulation, and its implications on society."
    SOCIAL_WORK = "I am a social worker, committed to enhancing the well-being of individuals and communities through counseling, advocacy, and social reforms."
    COMMUNICATION_ARTS_SCIENCES = "I am an expert in communication arts and sciences, well-versed in media studies, rhetoric, interpersonal communication, and the dynamics of human expression."
    AGRICULTURE_NATURAL_RESOURCES = "I am a specialist in agriculture and natural resources, with extensive knowledge in agronomy, sustainable farming practices, and the management of natural ecosystems."

    PROFILES = [
        {
            "title": "Architecture and Urban Planning",
            "description": ARCHITECTURE_URBAN_PLANNING,
        },
        {
            "title": "Art and Design",
            "description": ART_DESIGN,
        },
        {
            "title": "Dentistry",
            "description": DENTISTRY,
        },
        {
            "title": "Education",
            "description": EDUCATION,
        },
        {
            "title": "Engineering",
            "description": ENGINEERING,
        },
        {
            "title": "Environment and Sustainability",
            "description": ENVIRONMENT_SUSTAINABILITY,
        },
        {
            "title": "Information Science",
            "description": INFORMATION,
        },
        {
            "title": "Kinesiology",
            "description": KINESIOLOGY,
        },
        {
            "title": "Law",
            "description": LAW,
        },
        {
            "title": "Literature, Science, and the Arts",
            "description": LITERATURE_SCIENCE_ARTS,
        },
        {
            "title": "Medicine",
            "description": MEDICINE,
        },
        {
            "title": "Music, Theatre, and Dance",
            "description": MUSIC_THEATRE_DANCE,
        },
        {
            "title": "Nursing",
            "description": NURSING,
        },
        {
            "title": "Pharmacy",
            "description": PHARMACY,
        },
        {
            "title": "Public Health",
            "description": PUBLIC_HEALTH,
        },
        {
            "title": "Public Policy",
            "description": PUBLIC_POLICY,
        },
        {
            "title": "Social Work",
            "description": SOCIAL_WORK,
        },
        {
            "title": "Communication Arts and Sciences",
            "description": COMMUNICATION_ARTS_SCIENCES,
        },
        {
            "title": "Agriculture and Natural Resources",
            "description": AGRICULTURE_NATURAL_RESOURCES,
        },
    ]

    def __init__(self):
        client = chromadb.Client()
        self.collection = client.create_collection("expert_profiles")

        # make list of profile descriptions
        documents = []
        ids = []
        for profile in self.PROFILES:
            documents.append(profile["description"])
            ids.append(profile["title"])

        # Add docs to the collection. Can also update and delete. Row-based API coming soon!
        self.collection.add(
            documents=documents,
            ids=ids,
        )

    def query(self, query, n_results=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )
        return results
