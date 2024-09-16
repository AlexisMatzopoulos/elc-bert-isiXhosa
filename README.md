<h2 align="center"><b><h3>Investigating ELC-BERT for resource-efficient isiXhosa Language
Modeling</h3></b></h2><br>


<p align="center">
  <b>Alexis Matzopoulos</b>
  <b>mtzale001@myuct.ac.za</b>
</p>

<p align="center">
  <i>
    University of Cape Town<br>
  </i>
</p>
<br>


_______

<br>

<h3 align="center"><b>Abstract</b></h3><br>

This repository contains the code to pretrain the ELC-BERT architecture to the small WURA isiXhosa dataset, and subsequently finetunes the model on 3 finetuning tasks -NER, POS and NEWS, using the MasakhaNER organisation's isiXhosa datasets.

## Project Structure

We illustrate the project structure below. Before we proceed, it is imporant to point out that in training ELC-BERT isiXhosa, we make use of code from numerous repositories. We use some files from these repositories with and without modeification. all repositories we use allow us the permissions to use them. References for all these externally used repositories are provided below.

## Setup Instructions

### 1. Install Required Packages
Install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

### 2. Data download 
We provide the WURA xhosa datasets in the data/xhosa_raw folder. We upload this file directly as it contains a custom train/validation/test split. They dataset is also available at (https://huggingface.co/datasets/castorini/wura)

Before moving to the next step, first load the finetuning data for NER, POS and NEWS from MasakhaNER, MasakhaNEWS and MasakhaPOS resepctively by running the `python data_loader.py` file. This will download and save the data into the finetune_data folder.

### 2. Replicating our results

Here, we provide a guide of the steps to train and finetune our models to replicate our results. Each section contains its own detailed README, and so the purpose of this section here is the provide a high level guide of the order to proceed.

1. preprocess the data. Navigate to the preprocess folder for instructions. 

2. Create the tokenizer. Navigate to tokenizer folder for instructions.

3. cache our files for training. Navigate to the pre_training folder for instructions.

4. train our model. Navigate to train folder for instructions.

5. finetune our model NER, POS and NEWS tasks. Navigate to the finetune folder for instructions.

6. to generate heatmaps after you have trained your model, navigate to the heatmaps folder.

## Notes
Full Model weights and finetuning result files are both too large to be included in this Vula zip file upload. For interested parties, we will upload them on Github to use, otherwise one can replicate them by following the steps in this repo.

## References

ELC-BERT: 
Lucas Georges Gabriel Charpentier and David Samuel. 2023. Not all layers are equally as important: Every Layer Counts BERT. In <i>Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning</i>. Association for Computational Linguistics, Singapore, 238–252.

MasakhaNER:
David Adelani, Graham Neubig, Sebastian Ruder, Shruti Rijhwani, Michael Beukman, Chester Palen-Michel, Constantine Lignos, Jesujoba Alabi, Shamsuddeen Muhammad, Peter Nabende, Cheikh M. Bamba Dione, Andiswa Bukula, Rooweither Mabuya, Bonaventure F. P. Dossou, Blessing Sibanda, Happy Buzaaba, Jonathan Mukiibi, Godson Kalipe, Derguene Mbaye, Amelia Taylor, Fatoumata Kabore, Chris Chinenye Emezue, Anuoluwapo Aremu, Perez Ogayo, Catherine Gitau, Edwin Munkoh-Buabeng, Victoire Memdjokam Koagne, Allahsera Auguste Tapo, Tebogo Macucwa, Vukosi Marivate, Elvis Mboning Tchiaze, Tajuddeen Gwadabe, Tosin Adewumi, Orevaoghene Ahia, Joyce Nakatumba-Nabende, Neo Lerato Mokono, Ignatius Ezeani, Chiamaka Chukwuneke, Mofetoluwa Oluwaseun Adeyemi, Gilles Quentin Hacheme, Idris Abdulmumin, Odunayo Ogundepo, Oreen Yousuf, Tatiana Moteu, and Dietrich Klakow. 2022. MasakhaNER 2.0: Africa-centric Transfer Learning for Named Entity Recognition. In <i>Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing</i>. Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 4488–4508.

MasakhaNEWS:
David Ifeoluwa Adelani, Marek Masiak, Israel Abebe Azime, Jesujoba Oluwadara Alabi, Atnafu Lambebo Tonja, Christine Mwase, Odunayo Ogundepo, Bonaventure F. P. Dossou, Akintunde Oladipo, Doreen Nixdorf, Chris Chinenye Emezue, Sana Al-Azzawi, Blessing K. Sibanda, Davis David, Lolwethu Ndolela, Jonathan Mukiibi, Tunde Oluwaseyi Ajayi, Tatiana Moteu Ngoli, Brian Odhiambo, Abraham Toluwase Owodunni, Nnaemeka C. Obiefuna, Shamsuddeen Hassan Muhammad, Saheed Salahudeen Abdullahi, Mesay Gemeda Yigezu, Tajuddeen Rabiu Gwadabe, Idris Abdulmumin, Mahlet Taye Bame, Oluwabusayo Olufunke Awoyomi, Iyanuoluwa Shode, Tolulope Anu Adelani, Habiba Abdulganiy Kailani, Abdul-Hakeem Omotayo, Adetola Adeeko, Afolabi Abeeb, Anuoluwapo Aremu, Olanrewaju Samuel, Clemencia Siro, Wangari Kimotho, Onyekachi Raphael Ogbu, Chinedu E. Mbonu, Chiamaka I. Chukwuneke, Samuel Fanijo, Jessica Ojo, Oyinkansola F. Awosan, Tadesse Kebede Guge, Sakayo Toadoum Sari, Pamela Nyatsine, Freedmore Sidume, Oreen Yousuf, Mardiyyah Oduwole, Ussen Abre Kimanuka, Kanda Patrick Tshinu, Thina Diko, Siyanda Nxakama, Abdulmejid Tuni Johar, Sinodos Gebre, Muhidin Mohamed, S. A. Mohamed, Fuad Mire Hassan, Moges Ahmed Mehamed, Evrard Ngabire, and Pontus Stenetorp. 2023. MasakhaNEWS: News Topic Classification for African languages. In <i>Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing</i>.

MasakhaPOS:
Cheikh M. Bamba Dione, David Ifeoluwa Adelani, Peter Nabende, Jesujoba Alabi, Thapelo Sindane, Happy Buzaaba, Shamsuddeen Hassan Muhammad, Chris Chinenye Emezue, Perez Ogayo, Anuoluwapo Aremu, Catherine Gitau, Derguene Mbaye, Jonathan Mukiibi, Blessing Sibanda, Bonaventure F. P. Dossou, Andiswa Bukula, Rooweither Mabuya, Allahsera Auguste Tapo, Edwin Munkoh-Buabeng, Victoire Memdjokam Koagne, Fatoumata Ouoba Kabore, Amelia Taylor, Godson Kalipe, Tebogo Macucwa, Vukosi Marivate, Tajuddeen Gwadabe, Elvis Mboning Tchiaze, Ikechukwu Onyenwe, Gratien Atindogbe, Tolulope Adelani, Idris Akinade, Olanrewaju Samuel, Marien Nahimana, Théogène Musabeyezu, Emile Niyomutabazi, Ester Chimhenga, Kudzai Gotosa, Patrick Mizha, Apelete Agbolo, Seydou Traore, Chinedu Uchechukwu, Aliyu Yusuf, Muhammad Abdullahi, and Dietrich Klakow. 2023. MasakhaPOS: Part-of-Speech Tagging for Typologically Diverse African languages. In <i>Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</i>. Association for Computational Linguistics, Toronto, Canada, 10883–10900.

### Repos
ELC-BERT: https://github.com/ltgoslo/elc-bert/tree/main

MasakhaNER: https://github.com/masakhane-io/masakhane-ner/tree/main/MasakhaNER2.0

MasakhaNEWS: https://github.com/masakhane-io/masakhane-news

MasakhaPOS: https://github.com/masakhane-io/masakhane-pos

WURA: https://huggingface.co/datasets/castorini/wura



