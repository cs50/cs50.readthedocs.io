module Jekyll
  class Lecture < Liquid::Tag

    def initialize(tag_name, reference, tokens)
      super
      @reference = reference
      @lectures = {
        "2016/fall/0" => {
          "link" => "https://www.youtube.com/watch?v=o4SGkB_8fFs&list=PLhQjrBD2T382VRUw5ZpSxQSFrxMOdFObl",
          "title" => "Lecture 0"
        },
        "2016/fall/1" => {
          "link" => "https://www.youtube.com/watch?v=a8Fyf3gwvfM",
          "title" => "Lecture 1"
        },
        "2016/fall/2" => {
          "link" => "https://www.youtube.com/watch?v=2zPEHYoiyfc",
          "title" => "Lecture 3"
        }
      }
    end

    def render(context)
      if @reference.empty?
        return "Usage: {% lecture lecture_id %}"
      end
      @reference = @reference.to_s.strip
      "<a href='#{@lectures[@reference]["link"]}'>#{@lectures[@reference]["title"]}</a>"

    end
  end
end

Liquid::Template.register_tag('lecture', Jekyll::Lecture)
