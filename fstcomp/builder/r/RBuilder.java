package builder.r;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.StringTokenizer;

import tmp.generated_r.RParser;
import builder.ArtifactBuilder;
import cide.gparser.OffsetCharStream;
import cide.gparser.ParseException;
import de.ovgu.cide.fstgen.ast.FSTNonTerminal;

public class RBuilder extends ArtifactBuilder {
	public RBuilder() {
		super(".r");
	}

	public void processNode(FSTNonTerminal parent, StringTokenizer st,
			File inputFile) throws FileNotFoundException, ParseException {
		FSTNonTerminal rootDocument = new FSTNonTerminal("R-File", st
				.nextToken());
		parent.addChild(rootDocument);
		RParser rp = new RParser(new OffsetCharStream(
				new FileInputStream(inputFile)));
		
		rp.file_input(false);
		rootDocument.addChild(rp.getRoot());
	}
}
