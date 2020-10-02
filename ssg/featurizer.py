class Featurizer:
#     { 
#      "0 (current anchor)|+1 (the character on the right from anchor)|A (character)" : 1
#     }
        
    def __init__(self, N:int=2, sequence_size:int=1, delimiter:str='~')->None:
        self.N = N
        self.delimiter = delimiter
        self.radius = N + sequence_size
        pass
    
    def pad(self, sentence:str, padder:str='#')->str:
        return padder * (self.radius) + sentence + padder * (self.radius)

    def featurize(self, sentence:str, padding:bool=True, indiv_char:bool=True, return_type:str='list')->dict:
        if padding:
            sentence = self.pad(sentence)
        all_features = []
        all_labels = []
        skip_next = False
        for current_position in range(self.radius, len(sentence) - self.radius + 1):
            if skip_next:
                skip_next = False
                continue
            features = {}
            if return_type == 'list':
                features = []
            cut = 0
            char = sentence[current_position]
            if char == self.delimiter:
                cut = 1
                skip_next = True
            counter = 0
            chars_left = ''
            chars_right = ''
            chars = ''
            abs_index_left = current_position # left start at -1
            abs_index_right = current_position - 1 # right start at 0
            while counter < self.radius:
                abs_index_left -= 1 # สมมุติตำแหน่งที่ 0 จะได้ -1, -2, -3, -4, -5 (radius = 5)
                char_left = sentence[abs_index_left]
                while char_left == self.delimiter:
                    abs_index_left -= 1
                    char_left = sentence[abs_index_left]
                relative_index_left = -counter - 1
                # เก็บตัวหนังสือ
                chars_left = char_left + chars_left
                # ใส่ลง feature
                if indiv_char:
                    left_key = '|'.join([str(relative_index_left), char_left])
                    if return_type == 'dict':
                        features[left_key] = 1
                    else:
                        features.append(left_key)
                
                abs_index_right += 1 # สมมุติคือตำแหน่งที่ 0 จะได้ 0, 1, 2, 3, 4 (radius = 5)
                char_right = sentence[abs_index_right]
                while char_right == self.delimiter:
                    abs_index_right += 1
                    char_right = sentence[abs_index_right]
                relative_index_right = counter
                chars_right += char_right
                if indiv_char:
                    right_key = '|'.join([str(relative_index_right), char_right])
                    if return_type == 'dict':
                        features[right_key] = 1
                    else:
                        features.append(right_key)
                
                counter += 1
                
            chars = chars_left + chars_right
            for i in range(0, len(chars) - self.N + 1):
                ngram = chars[i:i + self.N]
                ngram_key = '|'.join([str(i - self.radius), ngram])
                if return_type == 'dict':
                    features[ngram_key] = 1
                else:
                    features.append(ngram_key)
            all_features.append(features)
            if(return_type == 'list'):
              cut = str(cut)
            all_labels.append(cut)
            
        return {
            'X': all_features,
            'Y': all_labels
        }
          
    def sentences_to_features(self, sentences:list, indiv_char:bool=False)->tuple:
        features = []
        labels = []
        for sentence in sentences:
            featurized = self.featurize(sentence, return_type='list', padding=True, indiv_char=indiv_char)
            features.append(featurized['X'])
            labels.append(featurized['Y'])
        return features, labels