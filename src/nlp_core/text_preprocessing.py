import re, string

from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.stopword import StopWord

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


class TextProcessing:
    def __init__(self,config) -> None:

        # self.stopword_en = stopwords.words("english")
        # self.stopword_id = StopWord.get_stopword()
        self.dataset_path = config["PATH_DATASET"]
    
    def case_folding(self, text:str)->str:
        '''fungsi yang digunakan untuk membersihkan teks'''

        result = text.lower()
        result = re.sub(r'\d+', '', result)
        result = re.sub(r'@[A-Za-z0-9]+', '', result)
        result = re.sub(r'https?:\/\/\w+.\w+', '', result)
        result = result.translate(str.maketrans('','',string.punctuation))
        result = result.strip()
        result = re.sub(r'  ',' ',result)

        return result
    
    def tokenisasi(self, text:str,mode:str='word')->list:
        '''fungsi yang digunakan untuk tokenisasi teks
        fungsi ini mempunyai dua mode
        word : melakukan token kata
        sentence : melakukan token kalimat 
        '''

        result = None

        if mode == 'word':
            token_ = PhraseTokenizer()
            result = token_.tokenize(text)
        elif mode == 'sentence':
            result = sent_tokenize(text)

        return result
    
    def lemmatisasi(self, text:str)->str:
        '''fungsi yang digunakan untuk lemmatisasi teks'''

        lemmatizer = Lemmatizer()
        result = lemmatizer.lemmatize(text)
        return result
    
    def hapus_stopword(self, text:str)->str:
        '''fungsi yang digunakan untuk menghapus stopword dari teks'''

        stopword = StopWord()
        result = stopword.remove_stopword(text)

        return result
    
if __name__ == '__main__':
    tp = TextProcessing()
    text = '''
    Datang ke Bandung tak lengkap rasanya kalau belum mencicipi makanan khas. Kamu pasti familiar kan dengan jajanan, seperti seblak, cuanki, siomay, ataupun cilok? Nah, jajanan tersebut memang jadi makanan khas Bandung yang sangat digemari serta mudah kamu temui di street food pinggir jalan.
    '''

    list_paragraf = tp.tokenisasi(text,mode='sentence')
    results = []
    for paragraf in list_paragraf:
        result = tp.case_folding(paragraf)
        result = tp.hapus_stopword(result)
        result = tp.lemmatisasi(result)

        results.append(result)
        
    print('.'.join(results))
        
