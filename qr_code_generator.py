import qrcode
import os

OUTPUT_FOLDER = "output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def generate_qr():
    print("\n===== QR Code Generator =====")

    data = input("Enter text or URL: ").strip()

    if not data:
        print("Input cannot be empty.")
        return

    filename = input("Enter file name (without extension): ").strip()

    if not filename:
        filename = "qr_code"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    path = os.path.join(OUTPUT_FOLDER, f"{filename}.png")

    image.save(path)

    print(f"\n✅ QR Code saved successfully!")
    print(f"Location: {path}")


while True:
    generate_qr()

    choice = input("\nGenerate another QR Code? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for using the QR Code Generator!")
        break