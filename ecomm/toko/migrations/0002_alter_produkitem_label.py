# Generated by Django 4.2 on 2023-04-11 23:20
from django.core.files import File
from django.db import migrations, models

def create_dummy_data(apps, schema_editor):
    ProdukItem = apps.get_model('toko', 'ProdukItem')
    image_path = 'product_pics/'
    # dummy_data = [
    # {
    #     'nama_produk': 'Samsung',
    #     'harga': 4500000,
    #     'harga_diskon': 500000,
    #     'slug': 'Hp-Samsung',
    #     'deskripsi': 'Samsung galaxy S20 penyimpanan 128 GB dan RAM 6GB.',
    #     'label': 'SALE',
    #     'kategori': 'electronics',
    #     'gambar_path': 'media/product_pics/hp samsung.jpg',
    # },
    # {
    #     'nama_produk': 'Lemari',
    #     'harga': 2300000,
    #     'harga_diskon': 250000,
    #     'slug': 'Lemari-3-pintu',
    #     'deskripsi': 'Lemari pakaian 3 pintu minimalis dengan bahan particle board dan dimensi 120 x 42 x 180.',
    #     'label': 'NEW',
    #     'kategori': 'home and kitchen',
    #     'gambar_path': 'media/product_pics/lemari.jpg',
    # },
    # # Add dummy data for the remaining instances
    # ]
    
    # for data in dummy_data:
    #     with open(data['gambar_path'], 'rb') as f:
    #         dummy_image = File(f)
    #         produk = ProdukItem(
    #             nama_produk=data['nama_produk'],
    #             harga=data['harga'],
    #             harga_diskon=data['harga_diskon'],
    #             slug=data['slug'],
    #             deskripsi=data['deskripsi'],
    #             label=data['label'],
    #             kategori=data['kategori'],
    #             gambar=dummy_image
    #     )
    #     produk.save()

    # produk_item1 = ProdukItem.objects.create(
    #     nama_produk='Samsung',
    #     harga=450,
    #     harga_diskon=50,
    #     slug='hp-samsung',
    #     deskripsi='Samsung galaxy S20 penyimpanan 128 GB dan RAM 6GB.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='SALE', 
    #     kategori='electronics'
    # )
    # produk_item2 = ProdukItem.objects.create(
    #     nama_produk='Lemari',
    #     harga=230,
    #     harga_diskon=25,
    #     slug='lemari-3-pintu',
    #     deskripsi='Lemari pakaian 3 pintu minimalis dengan bahan particle board dan dimensi 120 x 42 x 180.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='NEW',
    #     kategori='home'
    # )
    # produk_item3 = ProdukItem.objects.create(
    #     nama_produk='Tas bahu',
    #     harga=120,
    #     harga_diskon=2,
    #     slug='tas-charles&keith',
    #     deskripsi='Tas bahu Alcott yang dihiasi dengan syal yang dicetak, tas berukuran kecil dilengkapi dengan penutup ritsleting.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='BEST',
    #     kategori='fashion'
    # )
    # produk_item4 = ProdukItem.objects.create(
    #     nama_produk='Sepatu adidas',
    #     harga=40,
    #     harga_diskon=85,
    #     slug='sepatu-adidas',
    #     deskripsi='Bahan kulit dengan ukuran 36-42, kualitas sangat bagus.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='BEST',
    #     kategori='fashion'
    # )
    # produk_item5 = ProdukItem.objects.create(
    #     nama_produk='Philips Magic Com Rice Cooker 1.8L',
    #     harga=100,
    #     harga_diskon=10,
    #     slug='ricecooker-philips',
    #     deskripsi='Penanak nasi dengan Smart3D yang menghasilkan nasi dan hidangan lezat untuk semua keluarga.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='BEST',
    #     kategori='home'
    # )
    # produk_item6 = ProdukItem.objects.create(
    #     nama_produk='Flat Shoes',
    #     harga=35,
    #     harga_diskon=10,
    #     slug='sepatu-flat',
    #     deskripsi='Sepatu model loafers berbahan faux leather.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='NEW',
    #     kategori='fashion'
    # )
    # produk_item7 = ProdukItem.objects.create(
    #     nama_produk='HOKA Running Shoes',
    #     harga=135,
    #     harga_diskon=2,
    #     slug='sepatu-lari',
    #     deskripsi='Best for everyday running.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='BEST',
    #     kategori='fashion'
    # )
    # produk_item8 = ProdukItem.objects.create(
    #     nama_produk='Oppo A77 S',
    #     harga=350,
    #     harga_diskon=25,
    #     slug='hp-oppo',
    #     deskripsi='Hp Oppo dengan kamera 50MP dan RAM 8GB.',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='BEST',
    #     kategori='electronics'
    # )
    # produk_item9 = ProdukItem.objects.create(
    #     nama_produk='Toshiba LED TV - HD Smart TV 32"',
    #     harga=200,
    #     harga_diskon=15,
    #     slug='led-tv-toshiba',
    #     deskripsi='Smart TV yang dilengkapi dengan processor tercanggih',
    #     gambar= 'product_pics/pic1.jpg',
    #     label='NEW',
    #     kategori='electronics'
    # )
    
def create_dummy_data(apps, schema_editor):
    ProdukItem = apps.get_model('toko', 'ProdukItem')

    # Create dummy ProdukItems
    produk_item1 = ProdukItem.objects.create(
        nama_produk='Dummy Product 1',
        harga=10.99,
        harga_diskon=None,
        slug='dummy-product-1',
        deskripsi='This is a dummy product.',
        gambar='product_pics/lemari.jpg',
        label='NEW',
        kategori='A'
    )

    produk_item2 = ProdukItem.objects.create(
        nama_produk='Dummy Product 2',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-2',
        deskripsi='This is another dummy product.',
        gambar='product_pics/lemari.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item3 = ProdukItem.objects.create(
        nama_produk='Dummy Product 3',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-3',
        deskripsi='This is another dummy product.',
        gambar='product_pics/lemari.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item4 = ProdukItem.objects.create(
        nama_produk='Dummy Product 4',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-4',
        deskripsi='This is another dummy product.',
        gambar='product_pics/lemari.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item5 = ProdukItem.objects.create(
        nama_produk='Dummy Product 5',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-5',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy5.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item6 = ProdukItem.objects.create(
        nama_produk='Dummy Product 6',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-6',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy6.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item7 = ProdukItem.objects.create(
        nama_produk='Dummy Product 7',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-7',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy7.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item8 = ProdukItem.objects.create(
        nama_produk='Dummy Product 8',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-8',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy8.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item9 = ProdukItem.objects.create(
        nama_produk='Dummy Product 9',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-9',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy9.jpg',
        label='BEST',
        kategori='B'
    )
    produk_item10 = ProdukItem.objects.create(
        nama_produk='Dummy Product 9',
        harga=19.99,
        harga_diskon=15.99,
        slug='dummy-product-10',
        deskripsi='This is another dummy product.',
        gambar='product_pics/dummy9.jpg',
        label='BEST',
        kategori='B'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dummy_data),
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'primary'), ('SALE', 'info'), ('BEST', 'danger')], max_length=4),
        ),
    ]
