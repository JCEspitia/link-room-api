echo "BUILD START"
pip install --upgrade pip
python3.12 -m pip install -r requirements.txt

echo "Make migrations..."

python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"