import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.io.*;





public class winapp extends JFrame
{
  protected JList<String> listColors;
  protected draw drawer;
  protected JLabel labelR;
  protected JLabel labelG;
  protected JLabel labelB;
  protected JTextField tfR;
  protected JTextField tfG;
  protected JTextField tfB;
  protected JButton subR;
  protected JButton addR;
  protected JButton subG;
  protected JButton addG;
  protected JButton subB;
  protected JButton addB;
  protected JButton save;
  protected JButton reset;
  
  static Color colorvalue[]= new Color[11];
  static String colors[]= new String[11];
  protected Color c= colorvalue[0];
  protected int r=0;
  protected int g=0;
  protected int b=0;
  protected int i=0;
  
  
  private static final long serialVersionUID = 1000;
  
  

class draw extends JComponent
{
  public void paint(Graphics g)
  {
    Dimension d = getSize();
	
	g.setColor(c);
	g.fillRect(1,1,d.width-2,d.height-2);
	
	g.setColor(Color.black);
	g.drawRect(1,1,d.width-2,d.height-2);
  }
}
  
  
  
  public static void main (String argv []) throws IOException
  {
    new winapp("Color Sampler");
	
	//   input file name hard coded below
	FileInputStream stream = new FileInputStream("color.txt");  
	InputStreamReader reader = new InputStreamReader(stream); 
	StreamTokenizer tokens = new StreamTokenizer(reader); 
	
	String n;
	int r;
	int g;
    int b;
	int ind =0;
	
	while(tokens.nextToken() != tokens.TT_EOF)
	{
	  n=(String) tokens.sval;
	  tokens.nextToken();
	  r=(int) tokens.nval;
	  tokens.nextToken();
	  g=(int) tokens.nval;
	  tokens.nextToken();
	  b=(int) tokens.nval;
	  
	  colors[ind]=n;
	  colorvalue[ind]= new Color(r,g,b);
	  ind++;
    }
  }

  public winapp( String title)
  {
    super(title);
    setBounds(200,200,450,450);
    addWindowListener(new WindowDestroyer());
	
	
	drawer = new draw();
	labelR = new JLabel("Red:");
	labelG = new JLabel("Green:");
	labelB = new JLabel("Blue:");
	tfR = new JTextField(""+r);
	tfG = new JTextField(""+g);
	tfB = new JTextField(""+b);
	subR = new JButton("-");
	addR = new JButton("+");
	subG = new JButton("-");
	addG = new JButton("+");
	subB = new JButton("-");
	addB = new JButton("+");
	save = new JButton("Save");
	reset = new JButton("Reset");
	
	
	subR.addActionListener( new ActionHandler());
	addR.addActionListener( new ActionHandler());
	subG.addActionListener( new ActionHandler());
	addG.addActionListener( new ActionHandler());
	subB.addActionListener( new ActionHandler());
	addB.addActionListener( new ActionHandler());
	save.addActionListener( new ActionHandler());
	reset.addActionListener( new ActionHandler());

	// let’s also specify the arrangement of components by hand
	getContentPane().setLayout(null);
		
	getContentPane().add(drawer);
	getContentPane().add(labelR);
	getContentPane().add(labelG);
	getContentPane().add(labelB);
	getContentPane().add(tfR);
	getContentPane().add(tfG);
	getContentPane().add(tfB);
	
	getContentPane().add(subR);
	getContentPane().add(addR);
	getContentPane().add(subG);
	getContentPane().add(addG);
	getContentPane().add(subB);
	getContentPane().add(addB);
	getContentPane().add(save);
	getContentPane().add(reset);
		
	listColors= new JList<String>(colors);
	listColors.addListSelectionListener(new ListHandler());
	
	getContentPane().add(listColors);
	
	drawer.setBounds(10, 10, 270, 170);
	
	labelR.setBounds(40, 200, 50, 30);
	tfR.setBounds(100, 200, 50, 30);
	subR.setBounds(160,200,50,30);
	addR.setBounds(220,200,50,30);
	
	labelG.setBounds(40, 260, 50, 30);
	tfG.setBounds(100, 260, 50, 30);
	subG.setBounds(160,260,50,30);
	addG.setBounds(220,260,50,30);
	
	labelB.setBounds(40, 320, 50, 30);
	tfB.setBounds(100, 320, 50, 30);
	subB.setBounds(160,320,50,30);
	addB.setBounds(220,320,50,30);
	
	save.setBounds(90,360,70,30);
	reset.setBounds(180,360,70,30);
	
	
	listColors.setBounds(300,10,100,400);
	
	

    setVisible(true);
	repaint();
	

  }

  private class WindowDestroyer extends WindowAdapter
  {
    public void windowclosing(WindowEvent e)
    {
      System.exit(0);
    }
  }
  
  private class ListHandler implements ListSelectionListener
  {
    public void valueChanged(ListSelectionEvent e)
	{
	  if(e.getSource()== listColors)
	    if(!e.getValueIsAdjusting())
		{
		  i = listColors.getSelectedIndex();
		  String s = listColors.getSelectedValue();
		  c = colorvalue[i];
		  r = c.getRed();
		  g = c.getGreen();
		  b = c.getBlue();
		  repaint();
		  tfR.setText(""+r);
		  tfG.setText(""+g);
		  tfB.setText(""+b);
          
		}
    }
  }
  
  private class ActionHandler implements ActionListener
  {
    public void actionPerformed(ActionEvent e)
	{
	  if(e.getSource() == subR)
	  {
	    r= r-5;
		c= new Color(r,g,b);
		repaint();
		tfR.setText(""+r);
		newname("Color Sampler*");
	  }
	  else  if(e.getSource() == addR)
	  {
	    r= r+5;
		c= new Color(r,g,b);
		repaint();
		tfR.setText(""+r);
		newname("Color Sampler*");
	  }
	  else  if(e.getSource() == subG)
	  {
	    g= g-5;
		c= new Color(r,g,b);
		repaint();
		tfG.setText(""+g);
		newname("Color Sampler*");
	  }
	  else  if(e.getSource() == addG)
	  {
	    g= g+5;
		c= new Color(r,g,b);
		repaint();
		tfG.setText(""+g);
		newname("Color Sampler*");
	  }
	  else  if(e.getSource() == subB)
	  {
	    b= b-5;
		c= new Color(r,g,b);
		repaint();
		tfB.setText(""+b);
		newname("Color Sampler*");
	  }
	  else  if(e.getSource() == addB)
	  {
	    b= b+5;
		c= new Color(r,g,b);
		repaint();
		tfB.setText(""+b);
		newname("Color Sampler*");
	  }
	  else if (e.getSource() == reset)
	  {
	      c = colorvalue[i];
		  r = c.getRed();
		  g = c.getGreen();
		  b = c.getBlue();
		  repaint();
		  tfR.setText(""+r);
		  tfG.setText(""+g);
		  tfB.setText(""+b);
	  }
	  else if (e.getSource() == save)
	  {
	    colorvalue[i] = c;
		newname("Color Sampler");
	  }
	}
  }
	
  
  private void newname(String s)
  {
    this.setTitle(s);
  }

}