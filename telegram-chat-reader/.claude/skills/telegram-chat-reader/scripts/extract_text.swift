import Foundation
import PDFKit
import Vision

let arguments = CommandLine.arguments
guard arguments.count == 3 else { exit(2) }
let url = URL(fileURLWithPath: arguments[2])

do {
    switch arguments[1] {
    case "pdf":
        guard let document = PDFDocument(url: url), !document.isLocked else { exit(1) }
        var text = ""
        for index in 0..<document.pageCount {
            if let pageText = document.page(at: index)?.string {
                text += pageText + "\n"
                if text.count > 50_000 { break }
            }
        }
        print(String(text.prefix(50_001)), terminator: "")
    case "photo":
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        let supported = try request.supportedRecognitionLanguages()
        request.recognitionLanguages = supported.filter { $0 == "ru-RU" || $0 == "en-US" }
        try VNImageRequestHandler(url: url).perform([request])
        let text = (request.results ?? []).compactMap { $0.topCandidates(1).first?.string }
        print(text.joined(separator: "\n"), terminator: "")
    default:
        exit(2)
    }
} catch {
    exit(1)
}
