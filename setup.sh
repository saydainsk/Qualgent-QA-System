#!/bin/bash

echo "🔧 Starting setup for Qualgent-QA-System..."

# Step 1: Create virtual environment
echo "📦 Creating Python virtual environment (.venv)..."
python3 -m venv .venv

# Step 2: Activate virtual environment
echo "🧪 Activating environment..."
source .venv/bin/activate || source .venv/Scripts/activate

# Step 3: Upgrade pip
echo "🚀 Upgrading pip..."
pip install --upgrade pip

# Step 4: Install dependencies
echo "📦 Installing Python packages from requirements.txt..."
pip install -r requirements.txt

# Step 5: Clone Agent-S submodule if it's not already there
if [ ! -d "agent_s" ]; then
  echo "📥 Cloning Agent-S..."
  git clone https://github.com/saydainsk/Agent-S.git agent_s
else
  echo "✅ Agent-S already exists."
fi

# Step 6: Install android_world (from GitHub)
echo "📥 Installing android_env..."
pip install git+https://github.com/google-research/android_world.git

echo "✅ Setup complete! You can now run: source .venv/bin/activate && python test_run.py"
