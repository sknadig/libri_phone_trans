for s in dev_clean dev_other test_clean test_other train_clean_100 train_clean_360 train_other_500; do
    mv "$s"/text "$s"/text.orig
    python g2p.py new_lexicon "$s"/text.orig > "$s"/text;
done;