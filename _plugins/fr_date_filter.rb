require 'date'

module Jekyll
  module FrDateFilter
    MONTHS = {
      "January" => "Janvier", "February" => "Février", "March" => "Mars",
      "April" => "Avril", "May" => "Mai", "June" => "Juin",
      "July" => "Juillet", "August" => "Août", "September" => "Septembre",
      "October" => "Octobre", "November" => "Novembre", "December" => "Décembre"
    }

    def fr_date(input)
      date = input.is_a?(String) ? Date.parse(input) : input.to_date
      "#{date.strftime('%d')} #{MONTHS[date.strftime('%B')]} #{date.strftime('%Y')}"
    end
  end
end

Liquid::Template.register_filter(Jekyll::FrDateFilter)
