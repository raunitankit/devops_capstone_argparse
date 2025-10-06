# -------------------------------------------------
# 1️⃣ Base Image
# -------------------------------------------------
    FROM python:3.11-slim

    # -------------------------------------------------
    # 2️⃣ Set Working Directory
    # -------------------------------------------------
    WORKDIR /app
    
    # -------------------------------------------------
    # 3️⃣ Copy Files and Install Dependencies
    # -------------------------------------------------
    COPY . .
    RUN pip install --no-cache-dir .
    
    # -------------------------------------------------
    # 4️⃣ Set Default Command
    # -------------------------------------------------
    # This allows us to run with arguments like:
    # docker run capstone --limit 20
    ENTRYPOINT ["capstone"]