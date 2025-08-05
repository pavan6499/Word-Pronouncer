# 🗣️ Word Pronouncer

A web-based pronunciation learning tool that helps users learn to pronounce English words with an Indian English accent. The application breaks down words into two readable parts and provides interactive pronunciation practice.

## ✨ Features

- **Smart Word Splitting**: Automatically divides words into 2 meaningful, readable parts
- **Indian English Accent**: Prioritizes Indian English voices for authentic pronunciation
- **Interactive Learning**: Click individual parts to practice pronunciation
- **Visual Feedback**: Animated elements provide visual cues during pronunciation
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Speech**: Uses browser's built-in text-to-speech technology

## 🚀 Live Demo

Simply open the HTML file in any modern web browser to start using the Word Pronouncer.

## 🎯 How It Works

1. **Enter a Word**: Type any English word in the input field
2. **Automatic Analysis**: The word is intelligently split into 2 readable parts
3. **Practice Individual Parts**: Click each part to hear its pronunciation
4. **Sequential Practice**: Use "Practice Parts" to hear parts in sequence
5. **Full Word**: Click "Full Word" to hear the complete pronunciation

## 📱 Usage Examples

| Word | Part 1 | Part 2 |
|------|--------|--------|
| beautiful | beau | tiful |
| computer | com | puter |
| understand | under | stand |
| information | infor | mation |
| elephant | ele | phant |
| birthday | birth | day |

## 🎤 Voice Selection

The application uses a sophisticated voice selection algorithm that prioritizes:

1. **Native Indian English** (`en-IN`)
2. **Indian Voice Names** (Ravi, Aditi, Priya, Heera, etc.)
3. **Microsoft Indian Voices** (Windows)
4. **Google Indian Voices**
5. **British English** (closer to Indian pronunciation)
6. **Australian English** (alternative)
7. **High-quality English voices**

## 🔧 Technical Requirements

### Browser Support
- **Chrome/Chromium** (Recommended)
- **Firefox**
- **Safari**
- **Edge**
- **Mobile browsers**

### System Requirements
- Modern web browser with Speech Synthesis API support
- No additional installations required
- Works offline once loaded

## 🎨 Features Overview

### Core Functionality
- ✅ Word input and analysis
- ✅ Intelligent 2-part word splitting
- ✅ Individual part pronunciation
- ✅ Sequential pronunciation practice
- ✅ Full word pronunciation
- ✅ Visual feedback and animations

### Voice Features
- ✅ Indian English accent prioritization
- ✅ Comprehensive voice detection
- ✅ Fallback voice selection
- ✅ Speech quality optimization
- ✅ Error handling and recovery

### UI/UX Features
- ✅ Modern gradient design
- ✅ Responsive layout
- ✅ Interactive animations
- ✅ Loading states
- ✅ Error handling
- ✅ Mobile-friendly interface

## 🛠️ Installation

### Option 1: Direct Use
1. Save the HTML file to your computer
2. Open it in any modern web browser
3. Start using immediately - no setup required!

### Option 2: Web Server
1. Place the HTML file in your web server directory
2. Access via `http://yourserver.com/word-pronouncer.html`

### Option 3: Local Development
```bash
# Clone or download the file
# Open with live server (VS Code extension) or
python -m http.server 8000
# Then visit http://localhost:8000
```

## 🎵 Voice Optimization

### For Best Indian English Pronunciation:

**Windows Users:**
- Install Hindi language pack for Microsoft Heera/Kalpana voices
- Go to Settings > Time & Language > Language > Add Hindi

**Android Users:**
- Google Text-to-Speech usually includes Indian English voices
- Update Google app and Google Text-to-Speech

**Chrome Users:**
- Chrome often provides access to Google's online voices
- Ensure internet connection for best voice quality

## 🐛 Troubleshooting

### Common Issues:

**Voice Not Working:**
- Check browser permissions for audio
- Ensure speakers/headphones are connected
- Try refreshing the page
- Check browser console (F12) for voice information

**No Indian Accent:**
- Check console logs to see which voice is being used
- Install language packs on your system
- Try different browsers (Chrome recommended)

**Words Not Splitting Properly:**
- The algorithm handles 100+ common words with custom splits
- Less common words use intelligent splitting rules
- Complex words may need manual pronunciation practice

**Audio Cutting Off:**
- Increased timeouts should prevent this
- Try slower speech rate
- Check system audio settings

### Debug Information:
Open browser console (F12) to see:
- Which voice is being selected
- Available voices on your system
- Speech synthesis status
- Error messages if any

## 🤝 Contributing

This is a standalone HTML application. To contribute:

1. **Bug Reports**: Note browser, OS, and specific words causing issues
2. **Feature Requests**: Suggest improvements for pronunciation or UI
3. **Voice Improvements**: Share better voice selection strategies
4. **Word Database**: Suggest better splits for specific words

## 📝 Customization

### Adding Custom Word Splits:
Modify the `specialCases` object in the JavaScript code:

```javascript
const specialCases = {
    'yourword': ['your', 'word'],
    'customword': ['cus', 'tomword']
};
```

### Adjusting Voice Settings:
Modify the `speakText` function parameters:
- `rate`: Speech speed (0.1 to 10)
- `pitch`: Voice pitch (0 to 2)
- `volume`: Audio volume (0 to 1)

### Styling Changes:
The CSS uses modern techniques:
- CSS Grid and Flexbox for layout
- CSS custom properties for theming
- Responsive design with media queries

## 📊 Browser Compatibility

| Browser | Speech Synthesis | Indian Voices | Overall Support |
|---------|-----------------|---------------|-----------------|
| Chrome | ✅ Excellent | ✅ Good | ✅ Recommended |
| Firefox | ✅ Good | ⚠️ Limited | ✅ Supported |
| Safari | ✅ Good | ⚠️ Limited | ✅ Supported |
| Edge | ✅ Excellent | ✅ Good | ✅ Recommended |
| Mobile Chrome | ✅ Good | ✅ Good | ✅ Supported |
| Mobile Safari | ✅ Good | ⚠️ Limited | ✅ Supported |

## 🔐 Privacy & Security

- **No Data Collection**: All processing happens locally in your browser
- **No Server Communication**: Works completely offline after loading
- **No Personal Information**: Only the words you type are processed locally
- **Browser-Only Storage**: No data is stored or transmitted

## 📄 License

This project is open source and available under the MIT License.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 🙏 Acknowledgments

- Built with vanilla HTML, CSS, and JavaScript
- Uses Web Speech API for text-to-speech functionality
- Designed for English language learners, especially Indian English speakers
- Inspired by the need for accessible pronunciation learning tools

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Open browser console (F12) to see diagnostic information
3. Try different browsers or voice settings
4. Ensure your system has appropriate language packs installed

---

**Made with ❤️ for language learners worldwide** 🌍